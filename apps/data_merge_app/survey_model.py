import csv
from csv import DictWriter
from pathlib import Path
from typing import Optional

from pydantic import BaseModel

from .models.const import SHIFT_JIS
from .survey_data import SurveyData
from .survey_layout import SurveyLayout


class SurveyModel(BaseModel):
    data: SurveyData
    layout: SurveyLayout

    @classmethod
    def load_files(
        cls,
        sc_path: Optional[Path],
        main_dir_path: Path,
        sc_layout_path: Path,
        main_layout_dir_path: Path,
    ) -> "SurveyModel":
        data = SurveyData.load_files(sc_path, main_dir_path)
        layout = SurveyLayout.load_files(sc_layout_path, main_layout_dir_path)

        return cls(data=data, layout=layout)

    def output(
        self,
        output_path: Path,
        flag_names: Optional[list[str]] = None,
        attribute_conditions: Optional[list[tuple[int, dict[str, list[int]]]]] = None,
    ) -> None:
        if flag_names is None and attribute_conditions is None:
            if self.data.sc_data is None:
                field_names, output_data = self.data.merge_main_data()
            else:
                field_names, output_data = self.data.merge_data()

        else:
            if attribute_conditions is None:
                if self.data.sc_data is None:
                    field_names, output_data = self.data.merge_same_main_data_with_flag(
                        flag_names
                    )
                else:
                    raise ValueError("質問内容が同じかつSCデータがない時のみフラグをチェックしてください")
            else:
                if self.data.sc_data is None:
                    field_names, output_data = self.data.merge_main_data_with_flag(
                        attribute_conditions
                    )
                else:
                    raise ValueError("質問内容が同じかつSCデータがない時のみフラグをチェックしてください")

        with open(output_path, "w", encoding=SHIFT_JIS) as f:
            writer = DictWriter(f, fieldnames=field_names, delimiter="\t")
            writer.writeheader()
            writer.writerows(output_data)

    def output_layout(
        self, output_path: Path, flag_names: Optional[list[str]] = None
    ) -> None:
        if flag_names is None:
            if self.layout.sc_layout is None:
                output_layout = self.layout.merge_diff_main_layout()
            else:
                output_layout = self.layout.merge_layout()
        else:
            if self.layout.sc_layout is None:
                output_layout = self.layout.merge_layout_with_flag(flag_names)
            else:
                raise ValueError("質問内容が同じかつSCデータがない時のみフラグをチェックしてください")

        with open(output_path, "w", encoding="shift_jis") as f:
            writer = csv.writer(f, delimiter="\t")
            writer.writerows(output_layout)
