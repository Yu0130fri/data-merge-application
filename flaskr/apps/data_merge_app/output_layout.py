import csv
from pathlib import Path

from .models.merge_data import merge_data, merge_layout

_FIRST_ELEM = 0


def output_layout(sc_path: Path, main_path: Path, output_path: Path) -> None:
    merged_layout = merge_layout(sc_path=sc_path, main_path=main_path)

    with open(output_path, "w", encoding="shift_jis") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(merged_layout)
