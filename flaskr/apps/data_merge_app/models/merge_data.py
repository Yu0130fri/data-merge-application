from pathlib import Path

from .read_txt import read_main_data, read_sc_data


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
