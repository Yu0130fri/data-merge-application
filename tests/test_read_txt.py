from pathlib import Path

import pytest

from apps.data_merge_app.models import detect_encoding

# from apps.data_merge_app.models.read_txt import (
#     read_main_data,
#     read_sc_data,
#     read_sc_layout,
# )

_ABS_PATH = Path("tests/test_data").resolve()


@pytest.mark.skip(reason="テスト済み")
def test_detect_encoding() -> None:
    test_file_path = "test_data.txt"

    path = Path.joinpath(_ABS_PATH, test_file_path)

    detect_encoding.detect_encoding(path)


@pytest.mark.skip(reason="テスト済み")
def test_detect_encoding_with_error() -> None:
    test_utf8_file_path = "test_data_utf8.txt"

    path = Path.joinpath(_ABS_PATH, test_utf8_file_path)

    with pytest.raises(UnicodeError):
        detect_encoding.detect_encoding(path)


@pytest.mark.skip(reason="テスト済み")
def test_read_sc_data() -> None:
    test_file_path = "test_data.txt"
    path = Path.joinpath(_ABS_PATH, test_file_path)

    sc_data = read_sc_data(path)

    assert sc_data is not None


@pytest.mark.skip(reason="テスト済み")
def test_read_main_data() -> None:
    test_file_path = "test_data.txt"
    path = Path.joinpath(_ABS_PATH, test_file_path)

    main_data = read_main_data(path)

    assert main_data is not None


def test_read_sc_layout() -> None:
    test_file_path = "【SCR】418700000068_Layout.txt"
    path = Path.joinpath(_ABS_PATH, test_file_path)

    layout_rows = read_sc_layout(path)

    assert layout_rows is not None
    assert layout_rows[91][0] == "SC1"
    assert layout_rows[91][3] == "sc1"


def test_read_layout() -> None:
    test_file_path = "【SCR】418700000068_Layout.txt"
    path = Path.joinpath(_ABS_PATH, test_file_path)

    layout_rows = read_main_data(path)

    assert layout_rows is not None
