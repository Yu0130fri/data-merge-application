from pathlib import Path

from chardet import detect
from flask import flash

_shift_jis = "SHIFT_JIS"


def detect_encoding(path: Path) -> bool:
    with open(path, "rb") as f:
        c = f.read()
        encoding = detect(c)["encoding"]

    if encoding != _shift_jis:
        flash("this file is not 'shift_jis'. please change file")
    return True
