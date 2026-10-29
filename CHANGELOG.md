# Changelog

All notable changes to this project are documented here.
This project follows [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-10-28

### Added
- Decoders for base64 (padding-tolerant), hex, 8-bit binary and URL encoding.
- ROT-N (Caesar) decoding and ROT-1..25 brute force.
- `auto` mode that tries every decoder and shows readable results.
- `ctf-decode` command-line tool.
- Test suite (pytest) and CI on GitHub Actions.

### Security
- No known vulnerabilities in this release.
