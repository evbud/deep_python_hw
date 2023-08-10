import unittest
from hw_11.task_01 import Matrix


class TestMatrix(unittest.TestCase):

    def setUp(self) -> None:
        self.matrix_1 = [[1, 0, 3], [5, -2, 1], [5, 0, 2], [-4, -1, 7]]
        self.matrix_2 = [[3, 5], [-1, 6], [0, 7]]
        self.matrix_3 = [[1, 0, 3], [5, -2, 1], [5, 0, 2], [-4, -1, 7]]

    def test_matrix_init(self):
        self.assertEqual(Matrix([[1, 0, 3], [5, -2, 1], [5, 0, 2], [-4, -1, 7]]), Matrix(self.matrix_1))
        self.assertEqual(True, Matrix(self.matrix_2).columns == 2)
        self.assertEqual(False, Matrix(self.matrix_3).rows == 3)
        self.assertEqual(True, Matrix(self.matrix_3).rows == 4)

    def test_find_sum_matrix_elements(self):
        self.assertEqual(17, Matrix(self.matrix_1).sum_elements())
        self.assertEqual(20, Matrix(self.matrix_2).sum_elements())

    def test_eq_matrix(self):
        self.assertEqual(Matrix(self.matrix_1), Matrix(self.matrix_3))
        self.assertNotEqual(Matrix(self.matrix_1), Matrix(self.matrix_2))

    def test_sum_matrix(self):
        self.assertEqual(f'Сложение матриц невозможно, так как размеры матриц не равны!',
                         Matrix(self.matrix_1) + Matrix(self.matrix_2))
        self.assertEqual(Matrix([[2, 0, 6], [10, -4, 2], [10, 0, 4], [-8, -2, 14]]),
                         Matrix(self.matrix_1) + Matrix(self.matrix_3))

    def test_mult_matrix(self):
        self.assertEqual(Matrix([[3, 26], [17, 20], [15, 39], [-11, 23]]),
                         Matrix(self.matrix_1) * Matrix(self.matrix_2))
        self.assertEqual(f'Перемножение невозможно, так как число столбцов матрицы A не равно числу строк B!',
                         Matrix(self.matrix_1) * Matrix(self.matrix_3))


if __name__ == '__main__':
    unittest.main(verbosity=2)
