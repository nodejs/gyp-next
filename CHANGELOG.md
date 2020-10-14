# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [0.6.1] - 2020-10-14

### Fixed
- Correctly rename object files for absolute paths in MSVS generator.

## [0.6.0] - 2020-10-13

### Added
- The Makefile generator will now output shared libraries directly to the product
  directory on all platforms (previously only macOS).

## [0.5.0] - 2020-09-30

### Added
- Extended compile_commands_json generator to consider more file extensions than
  just `c` and `cc`. `cpp` and `cxx` are now supported.
- Source files with duplicate basenames are now supported.

### Removed
- The `--no-duplicate-basename-check` option was removed.
- The `msvs_enable_marmasm` configuration option was removed in favor of
  auto-inclusion of the "marmasm" sections for Windows on ARM.

## [0.4.0] - 2020-07-14

### Added
- Added support for passing arbitrary architectures to Xcode builds, enables `arm64` builds.

### Fixed
- Fixed a bug on Solaris where copying archives failed.

## [0.3.0] - 2020-06-06

### Added
- Added support for MSVC cross-compilation. This allows compilation on x64 for
  a Windows ARM target.

### Fixed
- Fixed XCode CLT version detection on macOS Catalina.

## [0.2.1] - 2020-05-05

### Fixed
- Relicensed to Node.js contributors.
- Fixed Windows bug introduced in v0.2.0.

## [0.2.0] - 2020-04-06

This is the first release of this project, based on https://chromium.googlesource.com/external/gyp
with changes made over the years in Node.js and node-gyp.

[Unreleased]: https://github.com/nodejs/gyp-next/compare/v0.6.1...HEAD
[0.6.1]: https://github.com/nodejs/gyp-next/compare/v0.6.0...v0.6.1
[0.6.0]: https://github.com/nodejs/gyp-next/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/nodejs/gyp-next/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/nodejs/gyp-next/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/nodejs/gyp-next/compare/v0.2.1...v0.3.0
[0.2.1]: https://github.com/nodejs/gyp-next/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/nodejs/gyp-next/releases/tag/v0.2.0
