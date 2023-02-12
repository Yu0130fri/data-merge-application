import os
from glob import glob
from pathlib import Path

from .read_txt import read_main_layout, read_sc_layout

_DETAIL_COLS = 91
_COMMON_COL_NUM = 0
_CURRENT_DIR = Path.cwd()


def merge_layout(sc_path: Path, main_dir_path: Path) -> list[list[str]]:
    """SCと本調査のレイアウトをマージする

    Args:
        sc_path (Path): SCのレイアウトがあるPath
        main_path (Path): 本調査のレイアウトがあるPath

    Returns:
        list[list[str]]: レイアウトの行を格納したリストの二次元配列
    """

    sc_layout = read_sc_layout(sc_path)
    main_layout = merge_main_layout(main_dir_path)

    header_list = [main_layout[_COMMON_COL_NUM]]
    sc_list = sc_layout[1:]
    main_list = main_layout[_DETAIL_COLS:]  # 本調査のデータは92行目から

    return header_list + sc_list + main_list


def merge_main_layout(main_dir_path: Path) -> list[list[str]]:
    """異なる本調査のレイアウトをマージする

    Args:
        main_dir_path (Path): 本調査のファイルが格納されたdir

    Returns:
        list[list[str]]: _description_
    """
    if not os.path.isdir(main_dir_path):
        raise ValueError("引数はディレクトリ形式で入力してください")

    merged_layout: list[list[str]] = []

    main_files = glob(str(main_dir_path.relative_to(_CURRENT_DIR)) + "/*.txt")

    valid_sample_num: int = 0
    for idx, file_name in enumerate(main_files):
        file_path = Path(file_name)
        layout_data = read_main_layout(file_path)
        common = _extract_common(layout_data)
        valid_sample_num += int(common[-1])
        if idx == 0:
            merged_layout = layout_data
        else:
            merged_layout += layout_data[_DETAIL_COLS:]

    merged_layout[_COMMON_COL_NUM][-1] = str(valid_sample_num)
    # レイアウトはマージした2次配列の重複を取り除くだけで良いため、重複を削除する
    merged_layout = _get_unique_list(merged_layout)

    return merged_layout


def _extract_common(layout_data: list[list[str]]) -> list[str]:
    """レイアウトの1行目だけ取り出す"""
    return layout_data[_COMMON_COL_NUM]


def _get_unique_list(data: list[list[str]]) -> list[list[str]]:
    seen = []
    return [x for x in data if x not in seen and not seen.append(x)]
