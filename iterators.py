from typing import Any

# Итерируемый объект - объект, по элементам которого мы проходимся.
# Итератор - объект, который проходится по этим элементам.

# Задание 1
# Сделать класс-итератор, который будет перебирать числа Фибоначчи в заданном количестве
# При этом числа должны генерироваться на лету, т.е. нельзя их сгенерировать пачкой (в списке) и потом отдавать

# Задание 2
# Написать класс-итератор, который будет возвращать простые множители (с повторениями)

# Задание 3
# Написать класс-итератор, который принимает на вход список и число N. На выходе он должен выдавать
# список, разбитый на части по N элементов в каждой. Например:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] -2-> [[1, 2], [3, 4], [5, 6], [7, 8], [9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9] -3-> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


class Repeater:
    value: Any
    max_count: int
    count: int = 0

    def __init__(self, value: Any, max_count: int) -> None:
        self.value = value
        self.max_count = max_count

    # Возвращаем итератор
    def __iter__(self):
        self.count = 0
        return self

    # Берём очередной элемент
    def __next__(self):
        if self.count == self.max_count:
            raise StopIteration
        self.count += 1
        return self.value


repeater = Repeater(5, 7)

for x in repeater:
    print(x)

print('---')

for x in repeater:
    print(x)
