import csv
import os
from glob import glob
from pathlib import Path
from typing import Optional

from flask import flash
from pydantic import BaseModel

from .main_layout import MainLayout
from .sc_layout import ScreeningLayout

_BASE_DIR = Path.cwd()

_VALID_SAMPLE_ELEM = 13
_DETAIL_COLS = 90
_COMMON_COL_NUM = 0

_FLAG_NAME = "HQ1"
_FLAG_NAME_SMALL = "hq1"


class SurveyLayout(BaseModel):
    sc_layout: Optional[ScreeningLayout]
    main_layout_list: list[MainLayout]

    @classmethod
    def load_files(cls, sc_path: Optional[Path], main_dir_path: Path) -> "SurveyLayout":
        if sc_path is None:
            sc_layout = None
        else:
            sc_layout = ScreeningLayout.load_file(sc_path)

        if not os.path.isdir(main_dir_path):
            raise ValueError("引数はディレクトリ形式で入力してください")

        main_files = sorted(glob(str(main_dir_path.relative_to(_BASE_DIR)) + "/*.txt"))

        main_layout_list: list[MainLayout] = []
        for file in main_files:
            layout = MainLayout.load_file(Path(file))
            main_layout_list.append(layout)

        return cls(sc_layout=sc_layout, main_layout_list=main_layout_list)

    def merge_diff_main_layout(self) -> list[list[str]]:
        """質問内容が異なる本調査のレイアウトマージ

        Returns:
            list[list[str]]: マージされたレイアウトを返す（有効サンプル数も計算）
        """
        valid_sample_num: int = 0
        for idx, main_layout in enumerate(self.main_layout_list):
            layout_data = main_layout.main_layout
            common = layout_data[_COMMON_COL_NUM]
            valid_sample_num += int(common[_VALID_SAMPLE_ELEM])
            if idx == 0:
                merged_layout = layout_data
            else:
                merged_layout += layout_data[_DETAIL_COLS:]

        merged_layout[_COMMON_COL_NUM][_VALID_SAMPLE_ELEM] = str(valid_sample_num)
        # レイアウトはマージした2次配列の重複を取り除くだけで良いため、重複を削除する
        merged_layout = _get_unique_list(merged_layout)

        return merged_layout

    def merge_layout(self) -> list[list[str]]:
        if self.sc_layout is None:
            raise ValueError("SCレイアウトを入れてください")

        sc_layout = self.sc_layout.sc_layout
        main_layout = self.merge_diff_main_layout()

        header_list = [main_layout[_COMMON_COL_NUM]]
        sc_list = sc_layout[1:]
        main_list = main_layout[_DETAIL_COLS:]  # 本調査のデータは92行目から

        return header_list + sc_list + main_list

    def merge_layout_with_flag(self, flag_names: list[str]) -> list[list[str]]:
        valid_sample_num: int = 0
        for idx, main_layout in enumerate(self.main_layout_list):
            layout_data = main_layout.main_layout
            common = layout_data[_COMMON_COL_NUM]
            valid_sample_num += int(common[_VALID_SAMPLE_ELEM])
            if idx == 0:
                merged_layout = layout_data
            else:
                merged_layout += layout_data[_DETAIL_COLS:]

        merged_layout[_COMMON_COL_NUM][_VALID_SAMPLE_ELEM] = str(valid_sample_num)
        # レイアウトはマージした2次配列の重複を取り除くだけで良いため、重複を削除する
        merged_layout = _get_unique_list(merged_layout)

        # flagのレイアウトを追加
        hq_layout_col: list[str] = [
            _FLAG_NAME,
            "S",
            _FLAG_NAME,
            _FLAG_NAME_SMALL,
            "SA",
            str(len(flag_names)),
            "99",  # 暫定的
            "",
            "割り付けフラグ",
        ]
        hq_layout_detail_cols: list[list[str]] = []
        for idx, flag_name in enumerate(flag_names):
            hq_layout_detail_cols.append(
                [
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    str(idx + 1),
                    flag_name,
                ]
            )
        merged_layout.append(hq_layout_col)
        merged_layout += hq_layout_detail_cols

        return merged_layout


def _get_unique_list(data: list[list[str]]) -> list[list[str]]:
    seen = []
    return [x for x in data if x not in seen and not seen.append(x)]
