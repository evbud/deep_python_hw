import pytest
from hw_11.task_01 import Matrix


@pytest.fixture
def matrix_1():
    return [[1, 0, 3], [5, -2, 1], [5, 0, 2], [-4, -1, 7]]


@pytest.fixture
def matrix_2():
    return [[3, 5], [-1, 6], [0, 7]]


@pytest.fixture
def matrix_3():
    return [[1, 0, 3], [5, -2, 1], [5, 0, 2], [-4, -1, 7]]


def test_matrix_init(matrix_1, matrix_2, matrix_3):
    assert Matrix([[1, 0, 3], [5, -2, 1], [5, 0, 2], [-4, -1, 7]]) == Matrix(matrix_1)
    assert Matrix(matrix_2).columns == 2
    assert Matrix(matrix_3).rows != 3
    assert Matrix(matrix_3).rows == 4


def test_find_sum_matrix_elements(matrix_1, matrix_2):
    assert Matrix(matrix_1).sum_elements() == 17
    assert Matrix(matrix_2).sum_elements() == 20


def test_eq_matrix(matrix_1, matrix_2, matrix_3):
    assert Matrix(matrix_1) == Matrix(matrix_3)
    assert Matrix(matrix_2) != Matrix(matrix_3)


def test_sum_matrix(matrix_1, matrix_2, matrix_3):
    assert Matrix(matrix_1) + Matrix(matrix_2) == f'Сложение матриц невозможно, так как размеры матриц не равны!'
    assert Matrix(matrix_1) + Matrix(matrix_3) == Matrix([[2, 0, 6], [10, -4, 2], [10, 0, 4], [-8, -2, 14]])


def test_mult_matrix(matrix_1, matrix_2, matrix_3):
    assert Matrix(matrix_1) * Matrix(matrix_2) == Matrix([[3, 26], [17, 20], [15, 39], [-11, 23]])
    assert Matrix(matrix_1) * Matrix(matrix_3) == f'Перемножение невозможно, ' \
                                                  f'так как число столбцов матрицы A не равно числу строк B!'


if __name__ == '__main__':
    pytest.main(['-v'])
