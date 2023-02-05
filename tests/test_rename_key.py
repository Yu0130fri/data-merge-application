import pytest
from src.models.rename_key import rename_sc_data_keys


@pytest.fixture
def sample_dict_row() -> dict[str, str]:
    return {
        "MID": "000000000",
        "q1": "xxx",
    }


def test_rename_sc_data_keys(sample_dict_row: dict[str, str]) -> None:
    rename_dict_row = rename_sc_data_keys(sample_dict_row)

    assert "sc1" in rename_dict_row
