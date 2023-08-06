from sympy import Rational
from regressionlib.experiments.matrix_utils import transpose_matrix
from regressionlib.experiments.matrix_utils import get_matrix_det


def get_minor(matrix: list[list[Rational]], row: int, column: int):
    new_matrix = matrix[:row] + matrix[row + 1:]
    for i in range(len(new_matrix)):
        new_matrix[i] = new_matrix[i][:column] + new_matrix[i][column + 1:]

    return get_matrix_det(new_matrix)


def get_alg_additions_matrix(matrix: list[list[Rational]]):
    additions_matrix = [[] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            minor = get_minor(matrix, i, j)
            additions_matrix[i].append(minor * (-1 if (i + j) % 2 == 1 else 1))

    return additions_matrix


def invert_matrix(matrix: list[list[Rational]]):
    det = get_matrix_det(matrix)
    additions_matrix = get_alg_additions_matrix(matrix)

    return [[x / det for x in line] for line in transpose_matrix(additions_matrix)]
