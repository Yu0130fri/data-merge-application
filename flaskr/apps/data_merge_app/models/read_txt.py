import csv

from chardet import detect
from flask import flash

from .rename_key import rename_sc_data_keys

_MID_NUM = 0
_shift_jis = "SHIFT_JIS"


def detect_encoding(path: str) -> bool:
    with open(path, "rb") as f:
        c = f.read()
        encoding = detect(c)["encoding"]

    if encoding != _shift_jis:
        flash("this file is not 'shift_jis'. please change file")
    return True


def read_sc_data(path: str) -> list[dict[str, str]]:
    if detect_encoding(path):
        with open(path, "r", encoding="shift_jis") as f:
            reader = csv.DictReader(f, delimiter="\t")
            sc_data = [rename_sc_data_keys(row) for row in reader]

    if len(sc_data) == 0:
        flash("no finding sc record")

    sc_data = sorted(sc_data, key=lambda x: list(x.keys())[_MID_NUM])

    return sc_data


def read_main_data(path: str) -> list[dict[str, str]]:
    if detect_encoding(path):
        with open(path, "r", encoding="shift_jis") as f:
            reader = csv.DictReader(f, delimiter="\t")
            main_data = [row for row in reader]

    if len(main_data) == 0:
        flash("no finding main record")

    main_data = sorted(main_data, key=lambda x: list(x.keys())[_MID_NUM])

    return main_data
