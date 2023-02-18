import csv
from pathlib import Path

from flask import flash
from pydantic import BaseModel

from ..models.const import SHIFT_JIS
from ..models.detect_encoding import detect_encoding


class MainLayout(BaseModel):
    main_layout: list[list[str]]

    @classmethod
    def load_file(cls, main_layout_path: Path) -> "MainLayout":
        if detect_encoding(main_layout_path):
            with open(main_layout_path, "r", encoding=SHIFT_JIS) as f:
                reader = csv.reader(f, delimiter="\t")
                main_layout = [row for row in reader]

        if len(main_layout) == 0:
            flash("Not Finding layout data")

        return cls(main_layout=main_layout)
