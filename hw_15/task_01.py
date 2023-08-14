# Задание
# Решить задачи, которые не успели решить на семинаре.
# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

import argparse
import ast
import logging

LOG_FILE = 'task_01.log'

logging.basicConfig(filename=LOG_FILE,
                    filemode='a',
                    format='Уровень: {levelname}, Дата: {asctime} Функция "{funcName}()": {msg}',
                    encoding='utf-8',
                    style='{',
                    level=logging.INFO)
log = logging.getLogger(__name__)


def parse():
    parser = argparse.ArgumentParser(prog='hw_15 класс Матрица',
                                     epilog='Операции с матрицами',
                                     description=f'Модуль содержит класс Матрица, производит простые '
                                                 f'матемастические операции с матрицами'
                                                 f'В качестве параметров через командную строку программа принимает'
                                                 f'3 параметра - '
                                                 f'Модуль записывает информации о произведенных действиях в файл'
                                                 f'{LOG_FILE}')
    parser.add_argument('-m1', '--matrix1', help='Матрица 1 вида "[[]]"')
    parser.add_argument('-m2', '--matrix2', help='Матрица 2 вида "[[]]"')
    parser.add_argument('-a', '--action', help='Математическая операция ("=", "+", "*", "sum")')

    args = parser.parse_args()

    if args.action == '=':
        return Matrix(convert_string_to_list(args.matrix1)) == Matrix(convert_string_to_list(args.matrix2))
    elif args.action == '+':
        return Matrix(convert_string_to_list(args.matrix1)) + Matrix(convert_string_to_list(args.matrix2))
    elif args.action == '*':
        return Matrix(convert_string_to_list(args.matrix1)) * Matrix(convert_string_to_list(args.matrix2))
    elif args.action == 'sum':
        return Matrix(convert_string_to_list(args.matrix1)).sum_elements()
    else:
        return log.error(f'Неверный ввод аргументов')


def convert_string_to_list(text: str) -> list:
    """Преобразование строки в список с помощью модуля ast"""
    result = ast.literal_eval(text)
    return result


class Matrix:
    """Класс Матрица"""

    def __init__(self, matrix: list[list[int | float]]):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

    def sum_elements(self):
        """Нахождение суммы элементов матрицы"""
        sum_el = 0
        for i in range(self.rows):
            for j in range(self.columns):
                sum_el += self.matrix[i][j]
        log.info(f'Нахождение суммы элементов матрицы {self.matrix}: {sum_el}')
        return sum_el

    def __str__(self):
        """Построчный вывод матрицы на печать"""
        print_matrix = ''
        for row in self.matrix:
            for element in row:
                print_matrix += ''.join(f' {element}')
            print_matrix += ''.join('\n')
        return print_matrix

    def __eq__(self, other):
        """Сравнение матриц на равенство
        Две матрицы одинаковой размерности называются равными, если равны их соответствующие элементы."""
        if self.matrix == other.matrix:
            log.info(f'Матрицы {self.matrix} и {other.matrix} равны')
            return self.matrix == other.matrix
        else:
            log.info(f'Матрицы {self.matrix} и {other.matrix} не равны')
            return self.matrix == other.matrix

    def __add__(self, other):
        """Сложение матриц одинаковой размерности"""
        if self.rows == other.rows and self.columns == other.columns:
            matrix_sum = [[self.matrix[i][j] + other.matrix[i][j]
                           for j in range(self.columns)]
                          for i in range(self.rows)]
            log.info(f'Сложение матриц {self.matrix} + {other.matrix} = {matrix_sum}')
            return Matrix(matrix_sum)
        else:
            log.error(f'Сложение матриц невозможно, так как размеры матриц не равны! '
                      f'[{self.rows}][{self.columns}] !=  [{other.rows}][{other.columns}]')
            return f'Сложение матриц невозможно, так как размеры матриц не равны!'

    def __mul__(self, other):
        """Перемножение матриц
        Матрицы A и B могут быть перемножены, если они совместимы
        в том смысле, что число столбцов матрицы A равно числу строк B"""
        if self.columns == other.rows:
            matrix_mult = [[sum(a * b for a, b in zip(self_row, other_column))
                            for other_column in zip(*other.matrix)]
                           for self_row in self.matrix]
            log.info(f'Перемножение матриц {self.matrix} * {other.matrix} = {matrix_mult}')
            return Matrix(matrix_mult)
        else:
            log.error(f'Перемножение невозможно, так как число столбцов матрицы A [{self.columns}] '
                      f'не равно числу строк B [{other.rows}]!')
            return f'Перемножение невозможно, так как число столбцов матрицы A не равно числу строк B!'

    def __repr__(self):
        return f'Matrix({self.matrix})'


if __name__ == '__main__':
    # matrix_1 = Matrix([[1, 0, 3], [5, -2, 1], [5, 0, 2], [-4, -1, 7]])
    # matrix_2 = Matrix([[3, 5], [-1, 6], [0, 7]])
    # matrix_3 = Matrix([[1, 0, 3], [5, -2, 1], [5, 0, 2], [-4, -1, 7]])
    #
    # print(matrix_1+matrix_2)
    # print(matrix_1 == matrix_3)
    # print(matrix_1 == matrix_2)
    # matrix_3.sum_elements()
    # print(matrix_1 + matrix_3)
    # print(matrix_1 * matrix_2)
    # print(matrix_1 * matrix_3)
    parse()

# Примеры запуска из консоли:
# python3 task_01.py -m1 '[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]' -m2 '[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]' -a '='
# python3 task_01.py -m1 '[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]' -m2 '[[1, 1, 1], [1, 1, 1], [1, 1, 1]]' -a '='
# python3 task_01.py -m1 '[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]' -m2 '[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]' -a '+'
# python3 task_01.py -m1 '[[1, 1, 1], [1, 1, 1]]' -m2 '[[1, 1, 1], [1, 1, 1], [1, 1, 1]]' -a '+'
# python3 task_01.py -m1 '[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]' -m2 '[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]' -a '*'
# python3 task_01.py -m1 '[[1, 1, 1], [1, 1, 1]]' -m2 '[[1, 1, 1], [1, 1, 1], [1, 1, 1]]' -a '*'
# python3 task_01.py -m1 '[[1, 0, 3], [5, -2, 1], [5, 0, 2], [-4, -1.9, 7]]' -a 'sum'
