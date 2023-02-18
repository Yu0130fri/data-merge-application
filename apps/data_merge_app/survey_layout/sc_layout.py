import csv
from pathlib import Path

from flask import flash
from pydantic import BaseModel

from ..models.const import SHIFT_JIS
from ..models.detect_encoding import detect_encoding

_QUESTION_NUMBER_COL = 0
_ITEM_NAME_COL = 2
_LABEL_COL = 3


class ScreeningLayout(BaseModel):
    sc_layout: list[list[str]]

    @classmethod
    def load_file(cls, sc_layout_path: Path) -> "ScreeningLayout":
        if detect_encoding(sc_layout_path):
            with open(sc_layout_path, "r", encoding=SHIFT_JIS) as f:
                reader = csv.reader(f, delimiter="\t")

                sc_layout: list[list[str]] = []
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

                    sc_layout.append(new_row)

        if len(sc_layout) == 0:
            flash("Not Finding layout data")

        return cls(sc_layout=sc_layout)
