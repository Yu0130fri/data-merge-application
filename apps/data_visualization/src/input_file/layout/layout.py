from csv import reader
from io import TextIOWrapper

from pydantic import BaseModel

from .question_info import (
    MatrixMultiAnswer,
    MatrixSingleAnswer,
    MultiAnswer,
    QuestionInfo,
    SingleAnswer,
)

_FIRST_ELEM_FOR_CHECK_VALUE = 0
_UNUSED_COL = 4
_QUESTION_TYPE_POSITION = 1


class LayoutFile(BaseModel):
    """question_detail (質問番号, 質問タイプ): 各設問のブロック"""

    question_detail: dict[tuple[str, str], list[list[str]]]

    @classmethod
    def from_stringio(cls, file: TextIOWrapper) -> "LayoutFile":
        records = reader(file, delimiter="\t")

        question_detail: dict[tuple[str, str], list[list[str]]] = {}
        question_block: list[list[str]] = []
        question_number_list: list[str] = []
        question_type_list: list[str] = []
        for idx, record in enumerate(records):
            if idx < _UNUSED_COL:  # 不要な列
                continue
            elif idx == _UNUSED_COL:  # SEXの列開始
                question_number_list.append(record[_FIRST_ELEM_FOR_CHECK_VALUE])  # 質問番号
                question_block.append(record)
                question_type_list.append(record[_QUESTION_TYPE_POSITION])
                continue
            elif record[_FIRST_ELEM_FOR_CHECK_VALUE] != "":
                question_number = question_number_list[-1]
                question_type = question_type_list[-1]
                question_detail[(question_number, question_type)] = question_block
                question_block = [record]
                question_number_list = [record[_FIRST_ELEM_FOR_CHECK_VALUE]]
                question_type_list = [record[_QUESTION_TYPE_POSITION]]
            else:
                question_block.append(record)
                continue

        # add last block
        question_number = question_number_list[-1]
        question_type = question_type_list[-1]
        question_detail[(question_number, question_type)] = question_block

        return LayoutFile(question_detail=question_detail)


class Layout(BaseModel):
    question_info_dict: dict[str, QuestionInfo]

    @classmethod
    def from_layout_file(cls, file: TextIOWrapper) -> "Layout":
        layout_file = LayoutFile.from_stringio(file)

        question_blocks = layout_file.question_detail

        question_info_dict: dict[str, QuestionInfo] = {}
        for (question_number, question_type), question_block in question_blocks.items():
            if question_type == "S":
                question_class = SingleAnswer.from_lists(question_block)

            elif question_type == "M":
                question_class = MultiAnswer.from_lists(question_block)

            elif question_type == "MTS":
                question_class = MatrixSingleAnswer.from_lists(question_block)

            elif question_type == "MTM":
                question_class = MatrixMultiAnswer.from_lists(question_block)

            else:
                continue

            question_info = QuestionInfo(
                question_number=question_number,
                question_type=question_type,
                question_detail=question_class,
            )
            question_info_dict[question_number] = question_info

        return Layout(question_info_dict=question_info_dict)
