from csv import DictWriter

from .models.merge_data import merge_data

_FIRST_ELEM = 0


def main(sc_path: str, main_path: str, output_path: str) -> None:
    merged_data = merge_data(sc_path=sc_path, main_path=main_path)

    header = merged_data[_FIRST_ELEM].keys()

    with open(output_path, "w", encoding="shift_jis") as f:
        writer = DictWriter(f, fieldnames=header, delimiter="\t")
        writer.writeheader()
        writer.writerows(merged_data)
