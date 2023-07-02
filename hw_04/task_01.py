# ✔ Напишите функцию для транспонирования матрицы


def matrix_transposition(matr):
    matr_transp = []
    for column in range(len(matr[0])):
        new_row = []
        for row in range(len(matr)):
            new_row.append(matr[row][column])
        matr_transp.append(new_row)
    return matr_transp


if __name__ == '__main__':
    matrixx = [[1, 2, 3, 4], [5, 6, 7, 8], [8, 9, 10, 11]]
    print(matrix_transposition(matrixx))
