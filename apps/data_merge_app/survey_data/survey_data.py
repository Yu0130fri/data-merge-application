import itertools
import os
from glob import glob
from pathlib import Path
from typing import Optional

from flask import flash
from pydantic import BaseModel

from .main_data import MainData
from .sc_data import ScreeningData

_BASE_DIR = Path.cwd()

_GET_DICT_KEYS = 0
_MID = "MID"
_HQ_NAME = "hq"


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

        screening_data = self.sc_data.sc_data

        all_sc_and_main_data_iter = itertools.product(screening_data, main_data)

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

    def _generate_main_data_with_attribute_flag(
        self,
        main_data: list[dict[str, str]],
        attribute_conditions: list[tuple[int, dict[str, list[int]]]],
    ) -> list[dict[str, str]]:
        """mainデータに属性の隠し設問を追加する

        Args:
            main_data (list[dict[str, str]]): 本調査データ
            attribute_conditions (list[tuple[str, dict[str, list[int]]]]):
                各flagの番号に対応した属性情報が格納されたリスト
        Returns:
            list[dict[str, str]]: フラグ設問が追加された本調査データ
        """
        main_data_with_flag: list[dict[str, str]] = []

        for hq_num, condition in attribute_conditions:
            if condition is None:
                flash("条件が取得できませんでした")
                raise ValueError()
            for row in main_data:
                all_condition: int = len(condition)

                count_condition: int = 0  # 条件の数をカウントし、全て条件に合致しているか判定する
                for key, value in condition.items():
                    if int(row[key]) in value:
                        count_condition += 1

                if count_condition == all_condition:
                    row[_HQ_NAME] = str(hq_num)
                else:
                    try:
                        if row[_HQ_NAME] != "":
                            continue
                        else:
                            row[_HQ_NAME] = ""
                    except Exception:
                        row[_HQ_NAME] = ""

                main_data_with_flag.append(row)

        return main_data_with_flag

    def merge_main_data_with_flag(
        self,
        attribute_conditions: list[tuple[int, Optional[dict[str, list[int]]]]],
        attribute_flg: bool = True,
    ) -> tuple[list[str], list[dict[str, str]]]:
        """同じ内容の本調査を属性（もしくは連番）でフラグを作成し、データのカラムに追加する

        Args:
            attribute_conditions (list[tuple[int, Optional[dict[str, list[int]]]]]):
                本調査のフラグ番号に対応した条件のtupleを格納したリスト
            attribute_flg(bool): 本調査属性を利用するかのフラグ（デフォルトは有）

        Examples:
            attribute_conditions: [
                (1, {"AGE", [20, 21, 22, ..., 29], "PRE": [1, 2]}),
                (2, {~})...
            ]
            ファイルごとに連番を振る場合はdict→Noneが入る

        Raises:
            ValueError: 条件がNoneのとき（本調査ファイルごとに属性をつけるとき）、
                ファイル数と連番の番号が一致しない時

        Returns:
            tuple[list[str], list[dict[str, str]]]: フラグ付した後のheader情報とフラグ付されてマージ済みの本調査データ
        """
        merged_main_data_with_flag: list[dict[str, str]] = []
        keys_list: list[str] = []

        main_data_lists = self.main_data_list

        if attribute_flg:
            for main_data_list in main_data_lists:
                main_data = main_data_list.main_data

                main_data_with_flag = self._generate_main_data_with_attribute_flag(
                    main_data, attribute_conditions=attribute_conditions  # type: ignore
                )
                keys_list += list(main_data_with_flag[_GET_DICT_KEYS].keys())
                merged_main_data_with_flag += main_data_with_flag

        else:
            if len(main_data_lists) != len(attribute_conditions):
                flash("アップロードした本調査とフラグ付けの名前の数が一致していません！")
                raise ValueError()

            for idx, m_data in enumerate(main_data_lists):
                main_data_with_flag = []
                for row in m_data.main_data:
                    row[_HQ_NAME] = str(idx + 1)
                    main_data_with_flag.append(row)
                keys_list += list(main_data_with_flag[_GET_DICT_KEYS].keys())

                merged_main_data_with_flag += main_data_with_flag

        unique_keys_list = list(dict.fromkeys(keys_list))

        return unique_keys_list, merged_main_data_with_flag
