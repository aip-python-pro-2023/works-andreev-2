from typing import List, Union, Optional

Number = Union[int, float]


def s(a: Number, b: Number) -> Number:
    res: Number = a + b
    return res


def d(a: Number, b: Number) -> Optional[Number]:
    if b == 0:
        return None
    res: Number = a / b
    return res


a: int = 5
print(a)
# PyCharm выведет предупреждение
# a = 'Ivanov Ivan'
# print(a)

print(s(7, 8.98))

nums: list[int] = [7, 5, 11, 9]
# nums = 8
# nums.append('dgfhj')
another_nums: List['int'] = [55, 78, 14, 60]

data: dict[str, int] = {'a': 8, 'b': 3}
# data['sfd'] = 'dsfgsd'
# data[3544] = 4654

info: tuple[str, str, int] = ('Ivanov', 'Ivan', 27)

result: int = s(7, 13)
