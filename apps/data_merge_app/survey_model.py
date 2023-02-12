from pathlib import Path
from typing import Optional

from pydantic import BaseModel


# TODO　データの持ち方をclassで保有しておくと便利そう
class SurveyModel(BaseModel):
    sc_data: Optional[list[dict[str, str]]]
    main_data: list[dict[str, str]]

    sc_layout: Optional[list[list[str]]]
    main_layout: list[list[str]]

    @classmethod
    def generate_data_from_path(
        sc_data_path: Path,
        main_data_path: Path,
        sc_layout_path: Path,
        sc_layout_path: Path,
    ) -> "SurveyModel":
        pass
