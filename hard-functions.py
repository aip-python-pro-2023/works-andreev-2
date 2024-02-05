from typing import Union, Callable, Any

Number = Union[int, float]


# Функция-декоратор
def logger(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        print('Function is called')
        result: Any = func(*args, **kwargs)
        print('Function call is done')
        return result
    return wrapper


@logger
def s(a: Number, b: Number) -> Number:
    res: Number = a + b
    return res


def get_multiplier(a: Number) -> Callable[[Number], Number]:
    def multiplier(b: Number) -> Number:
        return a * b
    return multiplier


@logger
def greet() -> None:
    print('Hello World!')


greet()


print(s(8, 10))
get_sum: Callable[[Number, Number], Number] = s
print(get_sum(9, 15))

nums: list[int] = [7, 9, 88, -7, -1, -9, 4, 56, 0]
nums.sort(key=lambda x: x ** 2)
print(nums)

print(list(map(lambda x: x ** 3, nums)))
print(list(filter(lambda x: x >= 0, nums)))

double = get_multiplier(2)
triple = get_multiplier(3)

print(double(5), triple(5))
