import json
import os
from functools import wraps
from random import randint
from typing import Callable


def check_parameters(func: Callable):
    min_num = 1
    max_num = 100
    min_tries = 1
    max_tries = 10

    @wraps(func)
    def wrapper(number: int, tries: int, *args, **kwargs):
        if number > max_num or number < min_num:
            number = randint(min_num, max_num)
        if tries > max_tries or tries < min_tries:
            tries = randint(min_tries, max_tries)
        result = func(number, tries, *args, **kwargs)
        return result

    return wrapper


def logger(func: Callable):
    file_name = f'{func.__name__}.json'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        json_dict = {'args': args, **kwargs, 'result': result}
        data.append(json_dict)
        with open(file_name, 'w', encoding='utf-8') as f1:
            json.dump(data, f1, indent=2, ensure_ascii=False)
        return result

    return wrapper


def exec_counter(num: int = 1):
    def deco(func: Callable):
        results = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return deco


@exec_counter(3)
@check_parameters
@logger
def guess_number(number: int, tries: int) -> Callable[[], None]:
    """Игра 'Угадай число'. В качестве аргументов укажите загаданное число (1-100)
    и количество попыток на его отгадывание(1-10)."""
    for i in range(1, tries + 1):
        print(f'Попытка №{i} из {tries}')
        num_input = int(input('Введите число: '))
        if num_input == number:
            print('Поздравляем! Вы угадали!')
            return f'Вы угадали число {number}'
        else:
            print(f'Загаданное число меньше' if num_input > number else f'Загаданное число больше')
    print(f'Вы не угадали число {number}')
    return f'Вы не угадали число {number}'


if __name__ == '__main__':
    game = guess_number(0, 0)
    print(game)
