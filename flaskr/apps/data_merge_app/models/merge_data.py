from pathlib import Path

from .read_txt import read_main_data, read_main_layout, read_sc_data, read_sc_layout

_DETAIL_COLS = 91


def merge_data(sc_path: Path, main_path: Path) -> list[dict[str, str]]:
    """SCデータと本調査のデータを結合する
    本調査のデータにないMIDは削除

    Args:
        sc_path (str): SCデータのパス
        main_path (str): 本調査データのパス

    Returns:
        list[dict[str, str]]: 結合された辞書型を格納したリスト
    """

    merged_dict_list: list[dict[str, str]] = []

    sc_data = read_sc_data(sc_path)
    main_data = read_main_data(main_path)

    for sc_dict in sc_data:
        merged_dict: dict[str, str] = {}
        sc_mid = sc_dict.get("MID")

        for main_dict in main_data:
            main_mid = main_dict.get("MID")

            if sc_mid == main_mid:
                merged_dict.update(sc_dict)
                merged_dict.update(main_dict)
                break

        if len(merged_dict) != 0:
            merged_dict_list.append(merged_dict)
        else:
            continue

    return merged_dict_list


def merge_layout(sc_path: Path, main_path: Path) -> list[list[str]]:
    """SCと本調査のレイアウトをマージする

    Args:
        sc_path (Path): SCのレイアウトがあるPath
        main_path (Path): 本調査のレイアウトがあるPath

    Returns:
        list[list[str]]: レイアウトの行を格納したリストの二次元配列
    """

    sc_layout = read_sc_layout(sc_path)
    main_layout = read_main_layout(main_path)

    header_list = [main_layout[0]]
    sc_list = sc_layout[1:]
    main_list = main_layout[_DETAIL_COLS:]  # 本調査のデータは92行目から

    return header_list + sc_list + main_list
