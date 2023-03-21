from pydantic import BaseModel

from .dimension import Dimension
from .measurement import Measurement


class QuestionDetail(BaseModel):
    dimension: Dimension
    measurement: Measurement
