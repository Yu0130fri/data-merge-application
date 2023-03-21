from pydantic import BaseModel


class Dimension(BaseModel):
    # 設問の各種情報を保持する
    # barプロットに必要な情報をとりあえず保持しておく
    question_description: str  # 設問文
    question_index: str  # 設問番号
    question_type: str  # 設問のタイプ
    question_labels: list[str]  # 選択肢の内容
