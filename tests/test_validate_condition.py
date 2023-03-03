import pytest

from apps.data_merge_app.models.validate_condition import validate_condition


@pytest.fixture
def sample_conditions() -> list[dict[str, list[int]]]:
    return [
        {
            "SEX": [1],
            "AGE": list(range(20, 30)),
        },
        {
            "SEX": [2],
            "AGE": list(range(30, 40)),
        },
    ]


@pytest.fixture
def sample_conditions_with_data_value_error() -> list[dict[str, list[int]]]:
    return [{"SEX": [3]}]


@pytest.fixture
def sample_conditions_with_attribute_name_error() -> list[dict[str, list[int]]]:
    return [{"hoge": [3]}]


def test_validate_condition(sample_conditions: list[dict[str, list[int]]]) -> None:
    validate_condition(sample_conditions)


def test_validate_condition_with_error(
    sample_conditions_with_data_value_error: list[dict[str, list[int]]]
) -> None:
    with pytest.raises(ValueError) as exc_info:
        validate_condition(sample_conditions_with_data_value_error)

    assert str(exc_info.value) == "不正な条件が検知されました"


def test_validate_condition_with_name_error(
    sample_conditions_with_attribute_name_error: list[dict[str, list[int]]]
) -> None:
    with pytest.raises(ValueError) as exc_info:
        validate_condition(sample_conditions_with_attribute_name_error)

    assert str(exc_info.value) == "不正な属性が検知されました"
