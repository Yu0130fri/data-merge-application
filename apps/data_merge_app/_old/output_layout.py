import csv
from pathlib import Path
from typing import Optional

from .merge_layout import merge_layout, merge_main_layout


def output_layout(
    sc_path: Optional[Path], main_dir_path: Path, output_path: Path
) -> None:
    if sc_path is None:
        merged_layout = merge_main_layout(main_dir_path)
    else:
        merged_layout = merge_layout(sc_path=sc_path, main_dir_path=main_dir_path)

    with open(output_path, "w", encoding="shift_jis") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(merged_layout)
