from csv import DictReader
from io import TextIOWrapper

from pydantic import BaseModel


class RawData(BaseModel):
    data: list[dict[str, str]]

    @classmethod
    def from_stringio(cls, file: TextIOWrapper) -> "RawData":
        records = DictReader(file, delimiter="\t")
        return cls(data=[row for row in records])
