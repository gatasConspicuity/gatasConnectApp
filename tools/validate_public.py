#!/usr/bin/env python3
"""Validate an exported public snapshot without access to private sources."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

FIXED = {"README.md", "LICENSE", "NOTICE", "THIRD_PARTY_NOTICES.md",
         "public-assets.json", "tools/validate_public.py", "docs/SCREENSHOTS.md",
         "docs/COMMUNITY_WELCOME.md", "docs/images/Discord-Logo-Blurple.png",
         ".github/ISSUE_TEMPLATE/bug_report.yml", ".github/ISSUE_TEMPLATE/config.yml"}
WORKFLOWS = {".github/workflows/pages.yml", ".github/workflows/validate.yml"}
SECRETS = re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH |ENCRYPTED )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[0-9A-Z]{16}')


def allowed(name):
    p = PurePosixPath(name)
    if p.is_absolute() or ".." in p.parts or "\\" in name:
        return False
    if name in FIXED or name in WORKFLOWS:
        return True
    if name in ("licenses/README.md", "licenses/catalog.json"):
        return True
    if len(p.parts) == 3 and p.parts[:2] == ("licenses", "texts") and p.suffix == ".txt":
        return True
    if name in {"docs/gallery/" + f for f in ("manifest.json", "index.html", "gallery.js", "style.css")}:
        return True
    if len(p.parts) == 5 and p.parts[:3] == ("docs", "gallery", "images") and p.suffix in (".png", ".jpg", ".jpeg"):
        return True
    return False


def validate(root, *, allow_preview=False):
    root = Path(root).resolve()
    manifest = json.loads((root / "public-assets.json").read_text())
    if manifest.get("preview", False) and not allow_preview:
        raise ValueError("Working-tree preview cannot be published; export the committed source first")
    if manifest["schema"] != 1 or not re.fullmatch(r"[0-9a-f]{40}", manifest["source_commit"]):
        raise ValueError("Invalid export provenance")
    files = manifest["files"]
    if not (FIXED - {"public-assets.json"}).issubset(files):
        raise ValueError("Required public files are missing")
    for name, digest in files.items():
        if not allowed(name) or name in WORKFLOWS or name == "public-assets.json":
            raise ValueError("Unexpected managed export path: " + name)
        path = root / name
        if any(parent.is_symlink() for parent in [path, *path.parents] if parent.is_relative_to(root)):
            raise ValueError("Public files must not use symlinks: " + name)
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError("Export hash mismatch: " + name)
    for path in root.rglob("*"):
        name = path.relative_to(root).as_posix()
        if name == ".git" or name.startswith(".git/"):
            continue
        if path.is_symlink():
            raise ValueError("Unexpected public symlink: " + name)
        if not path.is_file():
            continue
        if not allowed(name) or name not in {*files, "public-assets.json", *WORKFLOWS}:
            raise ValueError("Unmanaged or forbidden public file: " + name)
        if SECRETS.search(path.read_bytes()):
            raise ValueError("Possible credential in public file: " + name)
    gallery = json.loads((root / "docs/gallery/manifest.json").read_text())
    if gallery["repository"] != "https://github.com/gatasConspicuity/gatasConnectApp" or gallery["pagesUrl"] != "https://gatasConspicuity.github.io/gatasConnectApp/":
        raise ValueError("Gallery must use public URLs")
    expected_images = set()
    for platform in gallery["platforms"]:
        shots = platform["screenshots"]
        for shot in shots:
            name = "docs/gallery/" + shot["file"]
            if name not in files or name in expected_images or not allowed(name):
                raise ValueError("Invalid gallery image: " + name)
            expected_images.add(name)
            if files[name] != shot["sha256"]:
                raise ValueError("Gallery image hash mismatch: " + name)
        if platform.get("appStore"):
            raise ValueError("App Store upload profiles must stay private")
    if {n for n in files if n.startswith("docs/gallery/images/")} != expected_images:
        raise ValueError("Unlisted gallery images")
    print(f"Public snapshot verified: {len(files)} managed files, {len(expected_images)} images.")


if __name__ == "__main__":
    try:
        validate(Path(__file__).resolve().parents[1], allow_preview=sys.argv[1:] == ["--allow-preview"])
    except (ValueError, KeyError, OSError) as error:
        sys.exit(str(error))
