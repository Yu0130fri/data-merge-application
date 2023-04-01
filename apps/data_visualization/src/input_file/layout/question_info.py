from typing import Union

from pydantic import BaseModel

_ITEM_NAME_POSITION = 2
_LABEL_POSITION = 3
_OPTION_NUM_POSITION = 7
_DESCRIPTION_POSITION = 8


class SingleAnswer(BaseModel):
    label: str
    question_description: str
    option_dict: dict[str, str]

    @classmethod
    def from_lists(cls, question_lists: list[list[str]]) -> "SingleAnswer":
        option_dict: dict[str, str] = {}
        for idx, row in enumerate(question_lists):
            if idx == 0:
                label = row[_LABEL_POSITION]
                question_description = row[_DESCRIPTION_POSITION]
                continue
            else:
                option_num = row[_OPTION_NUM_POSITION]
                option_name = row[_DESCRIPTION_POSITION]
                option_dict[option_num] = option_name

        return cls(
            label=label,
            question_description=question_description,
            option_dict=option_dict,
        )


class MultiAnswer(BaseModel):
    labels: list[str]
    question_description: str
    option_dict: dict[str, str]

    @classmethod
    def from_lists(cls, question_lists: list[list[str]]) -> "MultiAnswer":
        option_dict: dict[str, str] = {}
        labels: list[str] = []
        for idx, row in enumerate(question_lists):
            if idx == 0:
                question_description = row[_DESCRIPTION_POSITION]
                continue
            else:
                labels.append(row[_LABEL_POSITION])
                option_num = row[_OPTION_NUM_POSITION]
                option_name = row[_DESCRIPTION_POSITION]
                option_dict[option_num] = option_name

        return cls(
            labels=labels,
            question_description=question_description,
            option_dict=option_dict,
        )


class MatrixSingleAnswer(BaseModel):
    question_description: str
    single_answer_dict: dict[str, SingleAnswer]  # item_name: SAclass

    @classmethod
    def from_lists(cls, question_lists: list[list[str]]) -> "MatrixSingleAnswer":
        question_blocks_dict: dict[str, list[list[str]]] = {}  # label: list[list]
        question_label_list: list[str] = []  # ラベルを一時的に格納しておく
        question_block: list[list[str]] = []
        for idx, row in enumerate(question_lists):
            if idx == 0:
                question_description = row[_DESCRIPTION_POSITION]
                continue
            elif idx == 1:
                question_label_list.append(row[_LABEL_POSITION])
                question_block.append(row)
                continue
            elif row[_LABEL_POSITION] != "":
                label = question_label_list[-1]
                question_blocks_dict[label] = question_block
                question_block = [row]
                question_label_list = [row[_LABEL_POSITION]]
            else:
                question_block.append(row)

        label = question_label_list[-1]
        question_blocks_dict[label] = question_block

        single_answer_dict: dict[str, SingleAnswer] = {}
        for label, single_question_block in question_blocks_dict.items():
            single_answer = SingleAnswer.from_lists(single_question_block)

            single_answer_dict[label] = single_answer

        return cls(
            question_description=question_description,
            single_answer_dict=single_answer_dict,
        )


class MatrixMultiAnswer(BaseModel):
    question_description: str
    multi_answer_dict: dict[list[str], MultiAnswer]  # labels: multiAnswer

    @classmethod
    def from_lists(cls, question_lists: list[list[str]]) -> "MatrixMultiAnswer":
        question_blocks_dict: dict[list[str], list[list[str]]] = {}  # label: list[list]
        question_block: list[list[str]] = []
        labels: list[str] = []
        for idx, row in enumerate(question_lists):
            if idx == 0:
                question_description = row[_DESCRIPTION_POSITION]
                continue
            elif idx == 1:
                question_block.append(row)
                continue
            elif row[_ITEM_NAME_POSITION] == "":
                question_blocks_dict[labels] = question_block
                labels = []
                question_block = [row]
            else:
                labels.append(row[_LABEL_POSITION])
                question_block.append(row)

        question_blocks_dict[labels] = question_block

        multi_answer_dict: dict[list[str], MultiAnswer] = {}
        for labels, multi_answer_block in question_blocks_dict.items():
            multi_answer = MultiAnswer.from_lists(multi_answer_block)
            multi_answer_dict[labels] = multi_answer

        return cls(
            question_description=question_description,
            multi_answer_dict=multi_answer_dict,
        )


class QuestionInfo(BaseModel):
    question_number: str
    question_type: str
    question_detail: Union[
        SingleAnswer, MultiAnswer, MatrixSingleAnswer, MatrixMultiAnswer
    ]
