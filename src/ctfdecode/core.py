"""Core decoding functions for common CTF encodings."""

from __future__ import annotations

import base64
import binascii
import string
import urllib.parse

__all__ = [
    "auto_decode",
    "decode_base64",
    "decode_binary",
    "decode_hex",
    "decode_url",
    "rot_bruteforce",
    "rot_n",
]


def decode_base64(data: str) -> str:
    """Decode a base64 string, tolerating missing padding."""
    cleaned = "".join(data.split())
    cleaned += "=" * (-len(cleaned) % 4)
    try:
        return base64.b64decode(cleaned, validate=True).decode("utf-8")
    except (binascii.Error, UnicodeDecodeError) as exc:
        raise ValueError(f"not valid base64: {exc}") from exc


def decode_hex(data: str) -> str:
    """Decode a hex string. Accepts spaces, colons and a leading 0x."""
    cleaned = data.strip().lower().removeprefix("0x")
    cleaned = cleaned.replace(" ", "").replace(":", "")
    try:
        return bytes.fromhex(cleaned).decode("utf-8")
    except (ValueError, UnicodeDecodeError) as exc:
        raise ValueError(f"not valid hex: {exc}") from exc


def decode_binary(data: str) -> str:
    """Decode space-separated (or continuous) 8-bit binary to text."""
    bits = "".join(data.split())
    if not bits or set(bits) - {"0", "1"} or len(bits) % 8:
        raise ValueError("not valid 8-bit binary")
    return "".join(chr(int(bits[i : i + 8], 2)) for i in range(0, len(bits), 8))


def decode_url(data: str) -> str:
    """Decode percent-encoded (URL) text."""
    return urllib.parse.unquote_plus(data)


def rot_n(data: str, n: int = 13) -> str:
    """Rotate letters by n positions (Caesar cipher). Non-letters are kept."""
    n %= 26
    lower, upper = string.ascii_lowercase, string.ascii_uppercase
    table = str.maketrans(
        lower + upper,
        lower[n:] + lower[:n] + upper[n:] + upper[:n],
    )
    return data.translate(table)


def rot_bruteforce(data: str) -> dict[int, str]:
    """Return every ROT-1..25 candidate, keyed by shift."""
    return {n: rot_n(data, n) for n in range(1, 26)}


def _looks_like_text(text: str) -> bool:
    if not text:
        return False
    printable = sum(ch in string.printable for ch in text)
    return printable / len(text) > 0.95


def auto_decode(data: str) -> dict[str, str]:
    """Try every decoder and return the ones that produce readable text."""
    results: dict[str, str] = {}
    for name, func in (
        ("base64", decode_base64),
        ("hex", decode_hex),
        ("binary", decode_binary),
    ):
        try:
            out = func(data)
        except ValueError:
            continue
        if _looks_like_text(out):
            results[name] = out
    if "%" in data:
        results["url"] = decode_url(data)
    results["rot13"] = rot_n(data, 13)
    return results
