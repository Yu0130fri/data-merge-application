import pytest
from pathlib import Path

from src.models.read_txt import detect_encoding, read_sc_data, read_main_data

_ABS_PATH = Path("tests/test_data").absolute()


def test_detect_encoding() -> None:
    test_file_path = "test_data.txt"

    path = Path.joinpath(_ABS_PATH, test_file_path)

    assert detect_encoding(path) is True


def test_detect_encoding_with_error() -> None:
    test_utf8_file_path = "test_data_utf8.txt"

    path = Path.joinpath(_ABS_PATH, test_utf8_file_path)

    with pytest.raises(UnicodeError):
        detect_encoding(path)


def test_read_sc_data() -> None:
    test_file_path = "test_data.txt"
    path = Path.joinpath(_ABS_PATH, test_file_path)

    sc_data = read_sc_data(path)

    assert sc_data is not None


def test_read_main_data() -> None:
    test_file_path = "test_data.txt"
    path = Path.joinpath(_ABS_PATH, test_file_path)

    main_data = read_main_data(path)

    assert main_data is not None
