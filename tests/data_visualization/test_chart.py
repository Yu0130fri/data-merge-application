from pathlib import Path

from apps.data_visualization.src.chart import Chart

_CURRENT_DIR = Path(__file__).absolute().parent.parent
_DATA_DIR = _CURRENT_DIR / "test_data"
_RAWDATA_DICT = _DATA_DIR / "test_main_data"
_LAYOUT_DICT = _DATA_DIR / "test_layout"


def test_query() -> None:
    rawdata_path = _RAWDATA_DICT / "test_chart_data.txt"
    layout_path = _LAYOUT_DICT / "test_for_chart_data.txt"
    chart = Chart.from_input_file(rawdata_path=rawdata_path, layout_path=layout_path)

    question_detail = chart.query("Q4")

    assert question_detail.dimension is not None
    assert question_detail.measurement.chart_data is not None
