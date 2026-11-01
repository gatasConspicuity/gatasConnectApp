# Third-party notices

Third-party components keep their own copyrights and license terms. The
proprietary GATAS Connect license does not restrict those independent grants.
Credits and full terms for the selected platform are available offline under
**About → Licenses and credits → Third-party software**. The native SwiftUI
Watch target embeds none of these libraries and includes project terms only.
The table below covers the Android and iOS codebase together; it is not a list
of libraries present in every app package.

| Component | Terms |
| --- | --- |
| COBS | [MIT License](licenses/texts/MIT.txt) |
| Compose Icons and Line Awesome | [MIT License](licenses/texts/MIT.txt) |
| SLF4J | [SLF4J MIT License](licenses/texts/SLF4J-MIT.txt) |
| Frameworks and networking | [Apache License 2.0](licenses/texts/Apache-2.0.txt) |
| Skia and Skiko | [Apache License 2.0](licenses/texts/Apache-2.0.txt), [Skia BSD License](licenses/texts/Skia-BSD.txt) |
| Adobe DNG SDK | [Adobe DNG SDK License Agreement](licenses/texts/Adobe-DNG-SDK.txt), [DNG Specification Patent License](licenses/texts/Adobe-DNG-Patent.txt) |
| Expat | [Expat MIT License](licenses/texts/Expat-MIT.txt) |
| HarfBuzz | [HarfBuzz License](licenses/texts/HarfBuzz.txt) |
| ICU | [ICU and Included Third-Party Licenses](licenses/texts/ICU.txt) |
| libpng | [PNG Reference Library License](licenses/texts/PNG.txt) |
| libjpeg-turbo and IJG | [libjpeg-turbo BSD License](licenses/texts/libjpeg-turbo-BSD.txt), [Independent JPEG Group Terms](licenses/texts/IJG.txt) |
| libwebp | [WebP BSD License](licenses/texts/WebP-BSD.txt), [WebP Patent Grant](licenses/texts/WebP-Patent.txt) |
| PIEX | [Apache License 2.0](licenses/texts/Apache-2.0.txt) |
| zlib | [zlib License](licenses/texts/zlib.txt), [Chromium BSD License](licenses/texts/Chromium-BSD.txt) |
| Wuffs and Skia adapters | [Apache License 2.0](licenses/texts/Apache-2.0.txt), [Skia Wuffs Adapter License](licenses/texts/Wuffs-Skia-BSD.txt) |
| Kotlin standard library | [Apache License 2.0](licenses/texts/Apache-2.0.txt), [Boost Software License 1.0](licenses/texts/Boost-1.0.txt), [ThreeTenBP BSD License](licenses/texts/ThreeTenBP-BSD.txt) |
| Kotlin/Native runtime (iOS) | [Apache License 2.0](licenses/texts/Apache-2.0.txt), [MIT License](licenses/texts/MIT.txt), [Boost Software License 1.0](licenses/texts/Boost-1.0.txt), [libbacktrace BSD License](licenses/texts/libbacktrace-BSD.txt), [Bounded Queue BSD License](licenses/texts/Bounded-Queue-BSD.txt) |

COBS is adapted from Fabian Dittmann's implementation, Copyright (c) 2022
Fabian Dittmann, under MIT. The original notice is also retained in the source.
Compose Icons is Copyright (c) 2021 DevSrSouza; Line Awesome is Copyright (c)
Icons8 and is used under MIT. Full component credits are in
[licenses/catalog.json](licenses/catalog.json) and the app's component pages.

This software is based in part on the work of the Independent JPEG Group.
This product includes DNG technology under license by Adobe Systems Incorporated.

Skia, Skiko and the Adobe DNG SDK permit commercial and proprietary use under
their respective terms. Adobe's agreement, patent notice, disclaimers and
commercial-distribution indemnification condition are retained in full.

The original GATAS logo was created by Ries van Twisk using AI. The newer app
icon was generated with Imagegen and adapted into platform assets. Third-party
brand artwork remains with its holders. No exclusive copyright is claimed
merely because an image was AI generated.

The separate GATAS firmware and external services retain their own terms.

Regenerate the app resources after updates with `python3 tools/licensing.py --write`.
