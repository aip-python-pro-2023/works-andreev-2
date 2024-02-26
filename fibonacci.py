# Задание 1
# Сделать класс-итератор, который будет перебирать числа Фибоначчи в заданном количестве
# При этом числа должны генерироваться на лету, т.е. нельзя их сгенерировать пачкой (в списке) и потом отдавать

class Fibonacci:
    count: int
    max_count: int
    a: int = 0
    b: int = 1

    def __init__(self, max_count: int) -> None:
        self.max_count = max_count

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count == self.max_count:
            raise StopIteration

        if self.count == 0:
            self.count += 1
            return 0
        elif self.count == 1:
            self.count += 1
            return 1

        self.count += 1
        self.a, self.b = self.b, self.a + self.b
        return self.b


for x in Fibonacci(100):
    print(x)
