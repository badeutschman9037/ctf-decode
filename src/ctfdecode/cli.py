"""Command-line interface for ctf-decode."""

from __future__ import annotations

import argparse
import sys

from . import __version__, core


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ctf-decode",
        description="Decode common CTF encodings (base64, hex, binary, URL, ROT-N).",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument(
        "mode",
        choices=["auto", "base64", "hex", "binary", "url", "rot", "rotall"],
        help="decoder to use ('auto' tries them all)",
    )
    parser.add_argument("data", nargs="?", help="input string (reads stdin if omitted)")
    parser.add_argument("-n", "--shift", type=int, default=13, help="shift for 'rot' mode")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    data = args.data if args.data is not None else sys.stdin.read().strip()

    try:
        if args.mode == "auto":
            for name, out in core.auto_decode(data).items():
                print(f"[{name}] {out}")
        elif args.mode == "rotall":
            for shift, out in core.rot_bruteforce(data).items():
                print(f"ROT{shift:>2}: {out}")
        elif args.mode == "rot":
            print(core.rot_n(data, args.shift))
        else:
            func = getattr(core, f"decode_{args.mode}")
            print(func(data))
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
