from collections import defaultdict
from pathlib import Path

from pydantic import BaseModel

from ..input_file.input_file import InputFile
from ..input_file.layout.question_info import (MatrixMultiAnswer,
                                               MatrixSingleAnswer, MultiAnswer,
                                               SingleAnswer)
from ..question_detail import QuestionDetail
from ..question_detail.dimension import Dimension
from ..question_detail.measurement import Measurement


class Chart(BaseModel):
    input_file: InputFile

    @classmethod
    def from_input_file(cls, rawdata_path: Path, layout_path: Path) -> "Chart":
        return cls(input_file=InputFile.load(rawdata_path, layout_path))

    def query(self, question_number: str) -> QuestionDetail:
        question_info = self.input_file.layout.question_info_dict[question_number]
        question_data = self.input_file.rawdata.data

        question_description = question_info.question_detail.question_description
        question_type = question_info.question_type
        question_detail = question_info.question_detail

        if type(question_detail) is SingleAnswer:
            option_data = list(question_detail.option_dict.values())
            question_label = [question_detail.label]
            chart_data = self._count_single_answer(question_detail.label, question_data)

        elif type(question_detail) is MultiAnswer:
            option_data = list(question_detail.option_dict.values())
            question_label = question_detail.labels
            chart_data = self._count_multi_answer(question_label, question_data)

        # TODO
        # マトリクス形式の場合の処理は後ほど検討する
        # elif (
        #     type(question_detail) is MatrixSingleAnswer
        #     or type(question_detail) is MatrixMultiAnswer
        # ):
        #     question_labels = list(question_detail.single_answer_dict.values())
        else:
            raise ValueError()

        dimension = Dimension(
            question_description=question_description,
            question_number=question_number,
            question_type=question_type,
            question_label=question_label,
            option_data=option_data,
        )
        measurement = Measurement(chart_data=chart_data)

        return QuestionDetail(dimension=dimension, measurement=measurement)

    def _count_single_answer(
        self, label: str, rawdata: list[dict[str, str]]
    ) -> dict[str, int]:
        calc_dict: dict[str, int] = defaultdict(int)
        for row in rawdata:
            checked_option = row[label]
            calc_dict[checked_option] += 1

        return calc_dict

    def _count_multi_answer(
        self, labels: list[str], rawdata: list[dict[str, str]]
    ) -> dict[str, int]:
        calc_dict: dict[str, int] = defaultdict(int)
        for row in rawdata:
            for label in labels:
                # その他のFAなどをskip
                if "t" in label:
                    continue
                calc_dict[label] += int(row[label])

        return calc_dict
