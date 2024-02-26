# Итератор - объект, который перебирает элементы набора данных

# iter() - возвращает итератор для набора данных
# next() - берёт следующий элемент через итератор

data = [1, 2, 3]

iterator = iter(data)

while True:
    try:
        x = next(iterator)
    except StopIteration:
        break
    
    print(x)

# for x in data:
#     print(x)

# for x in [1, 2, 3]:
#     print(x)
#
# for x in 4, 5, 6:
#     print(x)
#
# for key in {'a': 3, 'b': 7}:
#     print(key)
#
# for x in {4, 6, 3, 8, 1, 5}:
#     print(x)
#
# for line in open('ooad.md'):
#     print(line)
#
# for i in range(8, 11):
#     print(i)
