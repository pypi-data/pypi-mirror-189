from sympy import Rational


class MatrixMultiplicationError(Exception):
    pass


def matrix_multiplication(matrix1: list[list[Rational]], matrix2: list[list[Rational]]) -> list[list[Rational]]:
    if len(matrix1[0]) != len(matrix2):
        raise
    new_matrix = [[Rational(0) for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1[0])):
                new_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return new_matrix
