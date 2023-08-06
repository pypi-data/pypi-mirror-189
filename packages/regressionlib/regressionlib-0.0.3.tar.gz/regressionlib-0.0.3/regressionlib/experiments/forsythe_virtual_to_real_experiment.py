from sympy import Rational

from regressionlib.experiments.abstract_experiment import ExperimentException, InvalidValueException
from regressionlib.experiments.constants import MAX_R, MIN_R

from regressionlib.experiments.forsythe_polynomial_experiment import ForsythePolynomialExperiment, det_x, \
    ForsythePolynomialExperimentException
from regressionlib.experiments.matrix_utils import invert_matrix
from regressionlib.experiments.matrix_utils import matrix_multiplication


def det_x_real_to_virtual(n, x1: Rational, xn: Rational, z1: Rational, zn: Rational) -> \
        tuple[list[Rational], Rational, Rational]:
    a = (xn - x1) / (zn - z1)
    b = x1 - a * z1
    z = det_x(n, z1, zn)
    arr_x = [a * zi + b for zi in z]

    return arr_x, a, b


class ForsytheVirtualToRealExperimentException(ExperimentException):
    exception_codes: dict[int, str] = {
        200: '"R" value is not in range [' + str(MIN_R) + ', ' + str(MAX_R) + ']',
    }


class ForsytheVirtualToRealExperiment(ForsythePolynomialExperiment):
    def __init__(self, r: int, a: Rational, b: Rational, gamma: list[Rational]):
        self.a = a
        self.b = b
        self.r = r
        self.gamma = gamma

        if r < MIN_R or r > MAX_R:
            raise ForsythePolynomialExperimentException(200)

        try:
            self.check_for_numbers(gamma)
            self.check_for_numbers([a, b])
            self.check_for_int(r)
        except InvalidValueException:
            raise ForsythePolynomialExperimentException(700)

    def get_star_thetas(self, gamma: list[Rational], a_matrix: list[list[Rational]]) -> list[Rational]:
        return [a[0] for a in matrix_multiplication(invert_matrix(a_matrix), [[x] for x in gamma])]

    def get_star_var_thetas(self, a_matrix: list[list[Rational]], q_matrix: list[list[Rational]]) -> list[Rational]:
        var_thetas = []
        for i in range(self.r + 1):
            curr_var_theta = Rational(0)

            for j in range(self.r + 1 - i):
                part = Rational(0)
                for k in range(j + 1):
                    part += a_matrix[i][i + k] * q_matrix[i + k][i + j] * (
                        1 if k % 2 == 0 else -1) / self.a ** (
                                    2 * i + k)

                curr_var_theta += part ** 2
            var_thetas.append(curr_var_theta)

        return var_thetas

    def get_a_matrix(self) -> list[list[Rational]]:
        num_line = [1]
        matrix = [[Rational(0) for _ in range(self.r + 1)] for _ in range(self.r + 1)]
        for j in range(self.r + 1):
            new_line = []
            for i in range(len(num_line)):
                matrix[i][j] = num_line[i] * self.b ** (j - i) * self.a ** (j - (len(num_line) - 1 - i))

                if i != 0:
                    new_line.append(num_line[i - 1] + num_line[i])
                else:
                    new_line.append(1)

            new_line.append(1)
            num_line = new_line

        return matrix
