from pathlib import Path

from chardet import detect
from flask import flash

encoding_dict = {"SHIFT_JIS": "shift_jis", "ascii": "utf-8", "UTF-8": "utf-8"}


def detect_encoding(path: Path) -> bool:
    with open(path, "rb") as f:
        c = f.read()
        encoding = detect(c)["encoding"]

    if encoding not in encoding_dict:
        print("encoding", encoding)
        flash("this file is not 'shift_jis'. please change file")
    return True
