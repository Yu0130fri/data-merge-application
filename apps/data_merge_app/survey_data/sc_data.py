import csv
from pathlib import Path

from flask import flash
from pydantic import BaseModel

from ..models.detect_encoding import detect_encoding
from ..models.rename_key import rename_sc_data_keys

_SHIFT_JIS = "shift_jis"
_MID_NUM = 0


class ScreeningData(BaseModel):
    sc_data: list[dict[str, str]]

    @classmethod
    def load_file(cls, sc_path: Path) -> "ScreeningData":
        if detect_encoding(sc_path):
            with open(sc_path, "r", encoding=_SHIFT_JIS) as f:
                reader = csv.DictReader(f, delimiter="\t")
                sc_data = [rename_sc_data_keys(row) for row in reader]

            if len(sc_data) == 0:
                flash("no finding sc record")

            sc_data = sorted(sc_data, key=lambda x: list(x.keys())[_MID_NUM])

            return cls(sc_data=sc_data)
        else:
            flash("データのエンコードが不正です")
            raise ValueError()
