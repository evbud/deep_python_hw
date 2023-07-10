"""Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные  варианты и выведите 4 успешных расстановки."""

from random import randint

MIN_DECK_COORD = 1
MAX_DECK_COORD = 8


def check_queens(positions: list[list[int]]) -> bool:
    n = 8
    x = []
    y = []
    for i in range(n):
        x.append(positions[i][0])
        y.append(positions[i][1])

    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False

    if correct:
        return True
    else:
        return False


def generate_positions(num_pos: int) -> None:
    position = []
    n = 8
    count = 1
    while count <= num_pos:
        i = 0
        while i < n:
            x = randint(MIN_DECK_COORD, MAX_DECK_COORD)
            y = randint(MIN_DECK_COORD, MAX_DECK_COORD)
            if [x, y] not in position:
                position.append([x, y])
                i += 1
        if check_queens(position):
            print(position)
        position.clear()


if __name__ == '__main__':
    generate_positions(4)
