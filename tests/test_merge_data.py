from pathlib import Path

import pytest

from apps.data_merge_app._old.merge_data import merge_data, merge_main_data

_ABS_PATH = Path("tests/test_data").absolute()


@pytest.mark.skip(reason="テスト済みのため")
def test_merge_data() -> None:
    sc_path = Path.joinpath(_ABS_PATH, "test_data.txt")
    main_path = Path.joinpath(_ABS_PATH, "test_main_data.txt")

    merged_data = merge_data(sc_path, main_path)

    assert "1003552642" in merged_data


def test_merge_main_data() -> None:
    main_dir_path = _ABS_PATH.joinpath("test_main_data")
    print("main_dir_path", main_dir_path)

    keys, _ = merge_main_data(main_dir_path)

    assert sorted(keys) == ["a", "b", "c", "d"]


def test_merge_main_data_with_error() -> None:
    dummy_path = Path("xxx/xxx.py")

    with pytest.raises(ValueError) as exc_info:
        merge_main_data(dummy_path)

    assert str(exc_info.value) == "引数はディレクトリ形式で入力してください"
