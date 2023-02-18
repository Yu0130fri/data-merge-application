import csv
from pathlib import Path

from flask import flash

from ..models.detect_encoding import detect_encoding
from ..models.rename_key import rename_sc_data_keys

_MID_NUM = 0

_SHIFT_JIS = "shift_jis"

_QUESTION_NUMBER_COL = 0
_ITEM_NAME_COL = 2
_LABEL_COL = 3


def read_sc_data(path: Path) -> list[dict[str, str]]:
    if detect_encoding(path):
        with open(path, "r", encoding=_SHIFT_JIS) as f:
            reader = csv.DictReader(f, delimiter="\t")
            sc_data = [rename_sc_data_keys(row) for row in reader]

    if len(sc_data) == 0:
        flash("no finding sc record")

    sc_data = sorted(sc_data, key=lambda x: list(x.keys())[_MID_NUM])

    return sc_data


def read_main_data(path: Path) -> list[dict[str, str]]:
    if detect_encoding(path):
        with open(path, "r", encoding=_SHIFT_JIS) as f:
            reader = csv.DictReader(f, delimiter="\t")
            main_data = [row for row in reader]

    if len(main_data) == 0:
        flash("no finding main record")

    main_data = sorted(main_data, key=lambda x: list(x.keys())[_MID_NUM])

    return main_data


def read_sc_layout(path: Path) -> list[list[str]]:
    if detect_encoding(path):
        with open(path, "r", encoding=_SHIFT_JIS) as f:
            reader = csv.reader(f, delimiter="\t")

            layout_rows: list[list[str]] = []
            for row in reader:
                new_row: list[str] = []
                for idx, elem in enumerate(row):
                    if (
                        idx == _QUESTION_NUMBER_COL
                        or idx == _ITEM_NAME_COL
                        or idx == _LABEL_COL
                    ):
                        elem = elem.replace("q", "sc").replace("Q", "SC")
                    new_row.append(elem)

                layout_rows.append(new_row)

    if len(layout_rows) == 0:
        flash("Not Finding layout data")

    return layout_rows


def read_main_layout(path: Path) -> list[list[str]]:
    if detect_encoding(path):
        with open(path, "r", encoding=_SHIFT_JIS) as f:
            reader = csv.reader(f, delimiter="\t")
            layout_rows = [row for row in reader]

    if len(layout_rows) == 0:
        flash("Not Finding layout data")

    return layout_rows
