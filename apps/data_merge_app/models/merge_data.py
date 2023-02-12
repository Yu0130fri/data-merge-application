import itertools
import os
from glob import glob
from pathlib import Path

from .read_txt import read_main_data, read_sc_data

_GET_DICT_KEYS = 0
_CURRENT_DIR = Path.cwd()
_MID = "MID"


def merge_data(
    sc_path: Path, main_dir_path: Path
) -> tuple[list[str], list[dict[str, str]]]:
    """SCデータと本調査のデータを結合する
    本調査のデータにないMIDは削除

    Args:
        sc_path (Path): SCデータのパス
        main_dir_path (Path): 本調査データのディレクトリパス

    Returns:
        list[str]: ヘッダー用のユニークなカラム名を格納したリスト
        list[dict[str, str]]: 結合された辞書型を格納したリスト
    """

    sc_data = read_sc_data(sc_path)
    _, main_data = merge_main_data(main_dir_path)

    all_sc_and_main_data_iter = itertools.product(sc_data, main_data)

    merged_dict_list: list[dict[str, str]] = []
    unique_merged_keys_list: list[str] = []

    for sc_dict, main_dict in all_sc_and_main_data_iter:
        merged_dict: dict[str, str] = {}
        sc_mid = sc_dict.get(_MID)
        main_mid = main_dict.get(_MID)

        merged_dict_keys: list[str] = []
        if sc_mid == main_mid:
            merged_dict.update(sc_dict)
            merged_dict.update(main_dict)
            merged_dict_keys = list(merged_dict.keys())
        else:
            continue

        merged_dict_list.append(merged_dict)
        unique_merged_keys_list += merged_dict_keys

        # extract unique elem from unique_merged_keys_list
        unique_merged_keys_list = list(dict.fromkeys(unique_merged_keys_list))

    return unique_merged_keys_list, merged_dict_list


def merge_main_data(main_dir_path: Path) -> tuple[list[str], list[dict[str, str]]]:
    """1つ以上の本調査をマージする

    Args:
        main_dir_path (Path): 本調査データが格納されたディレクトリ

    Raises:
        ValueError: 引数のパスがdirではないとき

    Returns:
        tuple[list[str], list[dict[str, str]]]:
            uniqueな辞書型のキーを保有したリスト、辞書型で保有したデータを格納したリスト
    """

    if not os.path.isdir(main_dir_path):
        raise ValueError("引数はディレクトリ形式で入力してください")

    merged_main_data: list[dict[str, str]] = []
    keys_list: list[str] = []

    main_files = glob(str(main_dir_path.relative_to(_CURRENT_DIR)) + "/*.txt")
    for file_name in main_files:
        file_path = Path(file_name)
        main_data = read_main_data(file_path)

        keys_list += list(main_data[_GET_DICT_KEYS].keys())
        merged_main_data += main_data

    unique_keys_list = list(dict.fromkeys(keys_list))

    return unique_keys_list, merged_main_data
