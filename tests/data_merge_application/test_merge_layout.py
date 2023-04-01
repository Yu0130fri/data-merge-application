from pathlib import Path

from apps.data_merge_app.survey_layout.survey_layout import SurveyLayout

_ABS_PATH = Path("tests/test_data").absolute()


def test_merge_main_layout() -> None:
    main_dir_path = _ABS_PATH.joinpath("test_layout")

    main_layout = SurveyLayout.load_files(sc_path=None, main_dir_path=main_dir_path)

    merged_layout_data = main_layout.merge_layout()

    assert merged_layout_data[0][-1] == "400"
    assert merged_layout_data is not None
