# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# doctest,
# unittest,
# pytest.

MATRIX_1 = [[1, 0, 3], [5, -2, 1], [5, 0, 2], [-4, -1, 7]]
MATRIX_2 = [[3, 5], [-1, 6], [0, 7]]
MATRIX_3 = [[1, 0, 3], [5, -2, 1], [5, 0, 2], [-4, -1, 7]]


class Matrix:
    """Класс Матрица"""

    def __init__(self, matrix: list[list[int | float]]):
        """
        >>> Matrix(MATRIX_1)
        Matrix([[1, 0, 3], [5, -2, 1], [5, 0, 2], [-4, -1, 7]])
        >>> print(Matrix(MATRIX_2).columns == 2)
        True
        >>> print(Matrix(MATRIX_3).rows == 3)
        False
        >>> print(Matrix(MATRIX_3).rows == 4)
        True
        """
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

    def sum_elements(self):
        """
        Нахождение суммы элементов матрицы
        >>> Matrix(MATRIX_1).sum_elements()
        17
        >>> Matrix(MATRIX_2).sum_elements()
        20
        """
        sum_el = 0
        for i in range(self.rows):
            for j in range(self.columns):
                sum_el += self.matrix[i][j]
        return sum_el

    def __str__(self):
        """
        Построчный вывод матрицы на печать
        >>> print(Matrix(MATRIX_2))
         3 5
         -1 6
         0 7
        <BLANKLINE>
        """
        print_matrix = ''
        for row in self.matrix:
            for element in row:
                print_matrix += ''.join(f' {element}')
            print_matrix += ''.join('\n')
        return print_matrix

    def __eq__(self, other):
        """
        Сравнение матриц на равенство
        Две матрицы одинаковой размерности называются равными, если равны их соответствующие элементы.
        >>> print(Matrix(MATRIX_1) == Matrix(MATRIX_3))
        True
        >>> print(Matrix(MATRIX_1) == Matrix(MATRIX_2))
        False
        >>> print(Matrix(MATRIX_1) != Matrix(MATRIX_2))
        True
        """
        return self.matrix == other.matrix

    def __add__(self, other):
        """
        Сложение матриц одинаковой размерности
        >>> print(Matrix(MATRIX_1) + Matrix(MATRIX_2))
        Сложение матриц невозможно, так как размеры матриц не равны!
        >>> print(Matrix(MATRIX_1) + Matrix(MATRIX_3))
         2 0 6
         10 -4 2
         10 0 4
         -8 -2 14
        <BLANKLINE>
        """
        if self.rows == other.rows and self.columns == other.columns:
            matrix_sum = [[self.matrix[i][j] + other.matrix[i][j]
                           for j in range(self.columns)]
                          for i in range(self.rows)]
            return Matrix(matrix_sum)
        else:
            return f'Сложение матриц невозможно, так как размеры матриц не равны!'

    def __mul__(self, other):
        """
        Перемножение матриц
        Матрицы A и B могут быть перемножены, если они совместимы
        в том смысле, что число столбцов матрицы A равно числу строк B
        >>> print(Matrix(MATRIX_1) * Matrix(MATRIX_2))
         3 26
         17 20
         15 39
         -11 23
        <BLANKLINE>
        >>> print(Matrix(MATRIX_1) * Matrix(MATRIX_3))
        Перемножение невозможно, так как число столбцов матрицы A не равно числу строк B!
        """
        if self.columns == other.rows:
            matrix_mult = [[sum(a * b for a, b in zip(self_row, other_column))
                            for other_column in zip(*other.matrix)]
                           for self_row in self.matrix]
            return Matrix(matrix_mult)
        else:
            return f'Перемножение невозможно, так как число столбцов матрицы A не равно числу строк B!'

    def __repr__(self):
        """
        >>> print(repr(Matrix(MATRIX_1)))
        Matrix([[1, 0, 3], [5, -2, 1], [5, 0, 2], [-4, -1, 7]])
        """
        return f'Matrix({self.matrix})'


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
