# 72 = 2 * 2 * 2 * 3 * 3

def factorization(number):
    current = 2
    while current <= number ** 0.5:
        while number % current == 0:
            number //= current
            yield current
        current += 1
    if number > 1:
        yield number


x = int(input())
print(*factorization(x), sep='*')
