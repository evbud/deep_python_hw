# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
from os import path
from random import randint
from typing import Callable


def args_from_csv(file_csv: str = 'args.csv'):
    if not path.exists(file_csv):
        gen_args_csv('args.csv')

    def get_args_from_csv(func: Callable):
        with open(file_csv, 'r', encoding='utf-8') as f:
            csv_reader = list(csv.reader(f))
            result = []

        def wrapper():
            for line in csv_reader:
                result.append(func(float(line[0]), float(line[1]), float(line[2])))
            return result

        return wrapper

    return get_args_from_csv


def logger(func: Callable):
    file_name = f'{func.__name__}.json'
    if path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        json_dict = {'args': args, **kwargs, 'result': result}
        data.append(json_dict)
        with open(file_name, 'w', encoding='utf-8') as f1:
            json.dump(data, f1, indent=2, ensure_ascii=False)
        return result

    return wrapper


def gen_args_csv(file_csv: str, str_min: int = 100, str_max: int = 1000) -> None:
    with open(file_csv, 'w', newline='', encoding='utf-8') as f:
        rand_args = []
        for _ in range(randint(str_min, str_max)):
            rand_args.append([randint(-100, 100), randint(-100, 100), randint(-100, 100)])
        writer = csv.writer(f)
        writer.writerows(rand_args)


@args_from_csv('args.csv')
@logger
def quadratic_equation(a: float, b: float, c: float = 0) -> str:
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = -b / (2 * a)
        return f'Дискриминант равен нулю, значит уравнение имеет единственный корень: {x1}'
    elif d > 0:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        return f'Дискриминант больше нуля, значит уравнение имеет два корня: {[x1, x2]}'
    else:
        return f'Дискриминант отрицательный, поэтому корней нет'


if __name__ == '__main__':
    print(quadratic_equation())
