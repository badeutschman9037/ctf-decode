# ctf-decode

[![CI](https://github.com/badeutschman9037/ctf-decode/actions/workflows/ci.yml/badge.svg)](https://github.com/badeutschman9037/ctf-decode/actions/workflows/ci.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/badeutschman9037/ctf-decode/badge)](https://scorecard.dev/viewer/?uri=github.com/badeutschman9037/ctf-decode)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/YOUR_PROJECT_ID/badge)](https://www.bestpractices.dev/projects/YOUR_PROJECT_ID)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A small command-line tool that decodes the encodings you run into constantly
in Capture the Flag (CTF) competitions: base64, hex, binary, URL encoding and
ROT-N / Caesar ciphers. Its `auto` mode tries every decoder at once and shows
only the results that look like readable text.

## Install

Requires Python 3.10 or newer.

```
git clone https://github.com/badeutschman9037/ctf-decode.git
cd ctf-decode
pip install .
```

Releases are published on the [Releases page](../../releases).

## Usage

```
ctf-decode auto   "ZmxhZ3toZWxsb30="      # try everything
ctf-decode base64 "ZmxhZ3toZWxsb30"       # padding optional
ctf-decode hex    "66 6c 61 67"
ctf-decode binary "01101000 01101001"
ctf-decode url    "flag%7Bhi%7D"
ctf-decode rot    "synt{ebg}" -n 13
ctf-decode rotall "khoor"                 # brute-force all 25 shifts
echo "ZmxhZw==" | ctf-decode base64       # reads stdin
```

Invalid input prints an error and exits with status 1.

## Development

```
pip install -e ".[dev]"
ruff check src tests   # lint
pytest                 # tests
```

Every push and pull request runs lint and tests on GitHub Actions.

## Contributing

Bug reports and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).
Report bugs and feature requests in the [issue tracker](../../issues).

## Security

To report a vulnerability, see [SECURITY.md](SECURITY.md). Please don't open a
public issue for security problems.

## License

[MIT](LICENSE) © 2026 Brenden Deutschman
