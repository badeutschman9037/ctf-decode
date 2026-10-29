# Contributing to ctf-decode

Thanks for your interest in contributing!

## Reporting bugs and requesting features

Open an issue in the [issue tracker](../../issues). For bugs, include the
input you used, the output you got, and what you expected.

For security problems, follow [SECURITY.md](SECURITY.md) instead.

## Submitting changes

1. Fork the repository and create a branch from `main`.
2. Set up a dev environment:
   ```
   pip install -e ".[dev]"
   ```
3. Make your change and add tests for it in `tests/`. New functionality
   must come with tests.
4. Make sure lint and tests pass:
   ```
   ruff check src tests
   pytest
   ```
5. Open a pull request against `main`. CI runs the same checks automatically,
   and all checks must pass before a PR is merged.

## Coding standards

- Python 3.10+, formatted to the `ruff` rules in `pyproject.toml`.
- Keep functions small and documented with a docstring.
- Decoders must raise `ValueError` on invalid input rather than crash.
