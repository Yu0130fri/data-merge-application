import pytest
from pathlib import Path


from src.models.merge_data import merge_data

_ABS_PATH = Path("tests/test_data").absolute()


def test_merge_data() -> None:
    sc_path = Path.joinpath(_ABS_PATH, "test_data.txt")
    main_path = Path.joinpath(_ABS_PATH, "test_main_data.txt")

    merged_data = merge_data(sc_path, main_path)

    assert "1003552642" in merged_data
