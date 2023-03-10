from .const import ATTRIBUTE_DICT


def validate_condition(attribute_conditions: list[dict[str, list[int]]]) -> None:
    """指定された属性の条件をバリデーションする

    Args:
        attribute_conditions (list[dict[str, int]]): 属性情報が入ったリスト

    Raises:
        ValueError: 不正な属性が検知されたとき
        ValueError: 不正な条件が検知されたとき
    """
    for condition in attribute_conditions:
        if list(condition) > list(ATTRIBUTE_DICT):
            raise ValueError("不正な属性が検知されました")

        for key, value in condition.items():
            if set(value) > set(ATTRIBUTE_DICT[key]):
                raise ValueError("不正な条件が検知されました")
            if sum(value) >= sum(ATTRIBUTE_DICT[key]):
                raise ValueError("不正な条件が検知されました")
