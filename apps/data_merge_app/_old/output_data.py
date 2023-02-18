from csv import DictWriter
from pathlib import Path
from typing import Optional

from .merge_data import merge_data, merge_main_data


def output_data(
    sc_path: Optional[Path], main_dir_path: Path, output_path: Path
) -> None:
    if sc_path is None:
        merged_data_keys, merged_data = merge_main_data(main_dir_path=main_dir_path)
    else:
        merged_data_keys, merged_data = merge_data(
            sc_path=sc_path, main_dir_path=main_dir_path
        )

    with open(output_path, "w", encoding="shift_jis") as f:
        writer = DictWriter(f, fieldnames=merged_data_keys, delimiter="\t")
        writer.writeheader()
        writer.writerows(merged_data)
