from sympy import Rational


class NonSquareMatrixException(Exception):
    pass


def triangulation(matrix: list[list[Rational]]) -> tuple[list[list[Rational]], int]:
    new_matrix = [[x for x in line] for line in matrix]

    minus_coeff = 1
    for i in range(len(new_matrix) - 1):
        i_max = i
        for j in range(i, len(new_matrix)):
            if abs(new_matrix[j][i]) > abs(new_matrix[i_max][i]):
                i_max = j

        if new_matrix[i_max][i] == 0:
            continue

        if i != i_max:
            max_row = new_matrix.pop(i_max)
            i_row = new_matrix.pop(i)
            new_matrix.insert(i, max_row)
            new_matrix.insert(i_max, i_row)
            minus_coeff *= -1

        for j in range(i + 1, len(new_matrix)):
            coeff = new_matrix[j][i] / new_matrix[i][i]
            for k in range(len(new_matrix[0])):
                new_matrix[j][k] -= new_matrix[i][k] * coeff
    return new_matrix, minus_coeff


def get_matrix_det(matrix: list[list[Rational]]) -> Rational:
    if len(matrix) != len(matrix[0]):
        raise NonSquareMatrixException()

    triangular_matrix, minus_coeff = triangulation(matrix)
    det = Rational(1)
    for i in range(len(triangular_matrix)):
        det *= triangular_matrix[i][i]

    return det * minus_coeff
