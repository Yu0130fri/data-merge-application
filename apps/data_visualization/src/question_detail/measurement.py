from typing import Union

from pydantic import BaseModel


class Measurement(BaseModel):
    chart_data: list[Union[int, float]]  # データのカウント
