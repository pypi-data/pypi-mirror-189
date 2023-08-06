from sympy import Rational


def transpose_matrix(matrix: list[list[Rational]]):
    new_matrix = [[] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j].append(matrix[i][j])

    return new_matrix
