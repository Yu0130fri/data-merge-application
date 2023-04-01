from pathlib import Path

from apps.data_visualization.src.input_file.layout import Layout

_CURRENT_DIR = Path(__file__).parent.parent
TEST_DATA = _CURRENT_DIR / "test_data/test_layout"


@pytest.mark.skip(reason="already test in local")
def test_layout() -> None:
    filepath = TEST_DATA / "test_p.txt"
    with open(file=filepath, mode="r", encoding="sjis") as f:
        Layout.from_layout_file(f)
