"""Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""


def num_fib(n: int) -> list[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    print(*(num_fib(11)))
