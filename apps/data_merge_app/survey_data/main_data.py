import csv
from pathlib import Path

from flask import flash
from pydantic import BaseModel

from ..models.detect_encoding import detect_encoding

_SHIFT_JIS = "shift_jis"
_MID_NUM = 0


class MainData(BaseModel):
    main_data: list[dict[str, str]]

    @classmethod
    def load_main_data(cls, path: Path) -> "MainData":
        if detect_encoding(path):
            with open(path, "r", encoding=_SHIFT_JIS) as f:
                reader = csv.DictReader(f, delimiter="\t")
                main_data = [row for row in reader]

        if len(main_data) == 0:
            flash("no finding main record")

        main_data = sorted(main_data, key=lambda x: list(x.keys())[_MID_NUM])

        return cls(main_data=main_data)
