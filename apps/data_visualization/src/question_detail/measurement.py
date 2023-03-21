# from typing import Union

from pydantic import BaseModel


class Measurement(BaseModel):
    # 選択肢番号: データカウントのdict
    chart_data: dict[str, int]
