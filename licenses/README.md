# Third-party license texts

The project license is in `../LICENSE`. Third-party copyrights and grants
remain separate. `catalog.json` maps the components and their credits to the
original texts below. Each component has an explicit `platforms` list. Shared
terms are included once in each applicable app.

| File | Terms |
| --- | --- |
| [texts/Apache-2.0.txt](texts/Apache-2.0.txt) | Apache License 2.0 |
| [texts/MIT.txt](texts/MIT.txt) | MIT License |
| [texts/SLF4J-MIT.txt](texts/SLF4J-MIT.txt) | SLF4J MIT License |
| [texts/Skia-BSD.txt](texts/Skia-BSD.txt) | Skia BSD License |
| [texts/Adobe-DNG-SDK.txt](texts/Adobe-DNG-SDK.txt) | Adobe DNG SDK License Agreement |
| [texts/Adobe-DNG-Patent.txt](texts/Adobe-DNG-Patent.txt) | DNG Specification Patent License |
| [texts/Expat-MIT.txt](texts/Expat-MIT.txt) | Expat MIT License |
| [texts/HarfBuzz.txt](texts/HarfBuzz.txt) | HarfBuzz License |
| [texts/ICU.txt](texts/ICU.txt) | ICU and Included Third-Party Licenses |
| [texts/PNG.txt](texts/PNG.txt) | PNG Reference Library License |
| [texts/libjpeg-turbo-BSD.txt](texts/libjpeg-turbo-BSD.txt) | libjpeg-turbo BSD License |
| [texts/IJG.txt](texts/IJG.txt) | Independent JPEG Group Terms |
| [texts/WebP-BSD.txt](texts/WebP-BSD.txt) | WebP BSD License |
| [texts/WebP-Patent.txt](texts/WebP-Patent.txt) | WebP Patent Grant |
| [texts/zlib.txt](texts/zlib.txt) | zlib License |
| [texts/Chromium-BSD.txt](texts/Chromium-BSD.txt) | Chromium BSD License |
| [texts/Wuffs-Skia-BSD.txt](texts/Wuffs-Skia-BSD.txt) | Skia Wuffs Adapter License |
| [texts/Boost-1.0.txt](texts/Boost-1.0.txt) | Boost Software License 1.0 |
| [texts/ThreeTenBP-BSD.txt](texts/ThreeTenBP-BSD.txt) | ThreeTenBP BSD License |
| [texts/libbacktrace-BSD.txt](texts/libbacktrace-BSD.txt) | libbacktrace BSD License |
| [texts/Bounded-Queue-BSD.txt](texts/Bounded-Queue-BSD.txt) | Bounded Queue BSD License |

After changing a component, notice or text, run:

```sh
python3 tools/licensing.py --write
python3 tools/licensing.py --check
```

The app opens with a short overview. Full terms are available per component
on separate pages, offline. The generator includes only the selected platform's
components and referenced terms:

| Target | Generated resource | Third-party scope |
| --- | --- | --- |
| Android | `composeApp/src/androidMain/composeResources/files/legal-notices.json` | COBS, icons, SLF4J, frameworks and Kotlin standard-library additions |
| iPhone/iPad | `composeApp/src/iosMain/composeResources/files/legal-notices.json` | Shared libraries, native graphics stack and Kotlin/Native runtime additions |
| Watch | `iosApp/GatasWatchApp/legal-notices.json` | Project terms only; the native SwiftUI target embeds no Kotlin/Compose libraries |

Do not edit these generated resources by hand. The Android APK embeds
`libandroidx.graphics.path.so` (an Apache-licensed AndroidX library), not the
Skiko/Skia image stack shipped with the iOS app. Operating-system graphics
implementations are not redistributed as part of this APK.

Older dependency scans and superseded combined files are retained separately
with the project review records. They are not part of the app bundle.
