"""Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции."""

from random import randint, uniform

MIN_NUM = -1000
MAX_NUM = 1000


def rand_pares(num_str: int, file_name: str) -> None:

    with open(file_name, 'a', encoding='UTF-8') as f:
        for _ in range(num_str):
            f.write(f'{randint(MIN_NUM, MAX_NUM)} | {uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == '__main__':
    rand_pares(3, 'task_01.txt')
