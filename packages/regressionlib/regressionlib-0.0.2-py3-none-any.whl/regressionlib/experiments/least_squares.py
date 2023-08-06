from regressionlib.experiments.matrix_utils import get_matrix_det
from regressionlib.experiments.matrix_utils import invert_matrix
from regressionlib.experiments.matrix_utils import matrix_multiplication
from regressionlib.experiments.matrix_utils import transpose_matrix
from sympy import Rational


class DegeneratedMatrixException(Exception):
    pass


def least_squares(a_matrix: list[list[Rational]], y_matrix: list[list[Rational]]) -> list[list[Rational]]:
    a_matrix_transposed = transpose_matrix(a_matrix)

    theta1 = matrix_multiplication(a_matrix_transposed, a_matrix)
    det = get_matrix_det(theta1)
    if det == 0:
        raise DegeneratedMatrixException()

    theta2 = invert_matrix(theta1)
    theta3 = matrix_multiplication(theta2, a_matrix_transposed)

    theta4 = matrix_multiplication(theta3, y_matrix)

    return theta4
