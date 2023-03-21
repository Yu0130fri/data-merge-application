from pathlib import Path

from pydantic import BaseModel

from .layout import Layout
from .rawdata import RawData


class InputFile(BaseModel):
    rawdata: RawData
    layout: Layout

    @classmethod
    def load(cls, rawdata_path: Path, layout_path: Path) -> "InputFile":
        with open(file=rawdata_path, mode="r", encoding="sjis") as f:
            rawdata = RawData.from_stringio(f)

        with open(file=layout_path, mode="r", encoding="sjis") as f:
            layout = Layout.from_layout_file(f)

        return cls(rawdata=rawdata, layout=layout)
