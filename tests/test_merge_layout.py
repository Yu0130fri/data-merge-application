from pathlib import Path

import pytest

from apps.data_merge_app.models.merge_layout import merge_main_layout

_ABS_PATH = Path("tests/test_data").absolute()


def test_merge_main_layout() -> None:
    main_dir_path = _ABS_PATH.joinpath("test_layout")

    merged_layout_data = merge_main_layout(main_dir_path)

    assert merged_layout_data[0][-1] == "400"
    assert merged_layout_data is not None
