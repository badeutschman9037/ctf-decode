import pytest

from ctfdecode import core
from ctfdecode.cli import main


def test_base64():
    assert core.decode_base64("ZmxhZ3toZWxsb30=") == "flag{hello}"


def test_base64_missing_padding():
    assert core.decode_base64("ZmxhZ3toZWxsb30") == "flag{hello}"


def test_base64_invalid():
    with pytest.raises(ValueError):
        core.decode_base64("not base64!!")


def test_hex_variants():
    assert core.decode_hex("666c6167") == "flag"
    assert core.decode_hex("0x666c6167") == "flag"
    assert core.decode_hex("66 6c 61 67") == "flag"
    assert core.decode_hex("66:6c:61:67") == "flag"


def test_hex_invalid():
    with pytest.raises(ValueError):
        core.decode_hex("zz")


def test_binary():
    assert core.decode_binary("01101000 01101001") == "hi"


@pytest.mark.parametrize("bad", ["", "0110", "01102000"])
def test_binary_invalid(bad):
    with pytest.raises(ValueError):
        core.decode_binary(bad)


def test_url():
    assert core.decode_url("flag%7Bhi%20there%7D") == "flag{hi there}"


def test_rot13_roundtrip():
    assert core.rot_n("synt{ebg}", 13) == "flag{rot}"
    assert core.rot_n(core.rot_n("Hello, World!", 7), 19) == "Hello, World!"


def test_rot_bruteforce_has_25():
    results = core.rot_bruteforce("abc")
    assert len(results) == 25
    assert results[1] == "bcd"


def test_auto_decode_finds_base64():
    assert core.auto_decode("ZmxhZ3toZWxsb30=")["base64"] == "flag{hello}"


def test_cli_base64(capsys):
    assert main(["base64", "ZmxhZw=="]) == 0
    assert capsys.readouterr().out.strip() == "flag"


def test_cli_error(capsys):
    assert main(["hex", "zz"]) == 1
    assert "error" in capsys.readouterr().err
