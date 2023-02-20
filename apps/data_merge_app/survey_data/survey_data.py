import itertools
import os
from glob import glob
from pathlib import Path
from typing import Optional

from pydantic import BaseModel

from .main_data import MainData
from .sc_data import ScreeningData

_BASE_DIR = Path.cwd()

_GET_DICT_KEYS = 0
_MID = "MID"


class SurveyData(BaseModel):
    sc_data: Optional[ScreeningData]
    main_data_list: list[MainData]

    @classmethod
    def load_files(cls, sc_path: Optional[Path], main_dir_path: Path) -> "SurveyData":
        if sc_path is None:
            sc_data = None
        else:
            sc_data = ScreeningData.load_file(sc_path)

        if not os.path.isdir(main_dir_path):
            raise ValueError("引数はディレクトリ形式で入力してください")

        main_files = sorted(glob(str(main_dir_path.relative_to(_BASE_DIR)) + "/*.txt"))
        main_data_list: list[MainData] = []
        for file_name in main_files:
            main_data = MainData.load_main_data(Path(file_name))
            main_data_list.append(main_data)

        return cls(sc_data=sc_data, main_data_list=main_data_list)

    def merge_main_data(self) -> tuple[list[str], list[dict[str, str]]]:
        """本調査同士をマージする

        Returns:
            tuple[list[str], list[dict[str, str]]]: 出力する時のヘッダーとマージしたデータ
        """
        merged_main_data: list[dict[str, str]] = []
        keys_list: list[str] = []

        for main_data in self.main_data_list:
            main = main_data.main_data
            keys_list += list(main[_GET_DICT_KEYS].keys())
            merged_main_data += main

        unique_keys_list = list(dict.fromkeys(keys_list))

        return unique_keys_list, merged_main_data

    def merge_data(self) -> tuple[list[str], list[dict[str, str]]]:
        """SCデータと本調査のデータを結合する(本調査のデータにないMIDは削除)

        Raises:
            ValueError: SCデータが存在しない時（本調査同士のマージのみの場合はmerge_main_dataを利用するため）

        Returns:
            tuple[list[str], list[dict[str, str]]]:
                ヘッダー用のユニークなカラム名を格納したリストと結合された辞書型を格納したリスト
        """
        _, main_data = self.merge_main_data()

        if self.sc_data is None:
            raise ValueError("マージするSCデータが存在しません")

        all_sc_and_main_data_iter = itertools.product(self.sc_data.sc_data, main_data)

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

    def merge_same_main_data_with_flag(
        self, flag_names: list[str]
    ) -> tuple[list[str], list[dict[str, str]]]:
        merged_main_data_with_flag: list[dict[str, str]] = []
        keys_list: list[str] = []

        main_data_list = self.main_data_list

        if len(main_data_list) != len(flag_names):
            raise ValueError("アップロードした本調査とフラグ付けの名前の数が一致していません！")

        for idx, (main_data, _) in enumerate(zip(main_data_list, flag_names)):
            main_data_with_flag: list[dict[str, str]] = []
            for row in main_data.main_data:
                row["HQ1"] = str(idx + 1)
                main_data_with_flag.append(row)

            keys_list += list(main_data_with_flag[_GET_DICT_KEYS].keys())

            merged_main_data_with_flag += main_data_with_flag

        unique_keys_list = list(dict.fromkeys(keys_list))

        return unique_keys_list, merged_main_data_with_flag
