from typing import Any

from sympy import Rational, Number
from sympy.core.numbers import One, Zero, Integer, NegativeOne, Half

from regressionlib.experiments.constants import PRECISION, MIN_PRECISION, MAX_PRECISION
from regressionlib.experiments.forsythe_polynomial_experiment import ForsythePolynomialExperiment, det_x
from regressionlib.experiments.forsythe_virtual_to_real_experiment import ForsytheVirtualToRealExperiment, \
    det_x_real_to_virtual
from regressionlib.experiments.multivariate_linear_regression_experiment import MultivariateLinearRegressionExperiment
from regressionlib.experiments.univariate_linear_regression_experiment import UnivariateLinearRegressionExperiment
from regressionlib.experiments.univariate_polynomial_regression_experiment import \
    UnivariatePolynomialRegressionExperiment
from regressionlib.experiments.utils import rational_to_float


def RA_univariate_linear(n: int, tx: list[Rational], ty: list[Rational]) -> tuple[Rational, Rational]:
    experiment = UnivariateLinearRegressionExperiment(n, tx, ty)
    return experiment.get_experiment_result()


def RA_multivariate_linear(n: int, m: int, x: list[list[Rational]], ty: list[Rational]) -> list[Rational]:
    experiment = MultivariateLinearRegressionExperiment(n, m, x, ty)
    return experiment.get_experiment_result()


def RA_univariate_polynomial(n: int, r: int, tx: list[Rational], ty: list[Rational]) -> list[Rational]:
    experiment = UnivariatePolynomialRegressionExperiment(n, r, tx, ty)
    return experiment.get_experiment_result()


def RA_Forsythe_uniform(n: int, r: int, x1: Rational, xn: Rational) -> list[list[Rational]]:
    experiment = ForsythePolynomialExperiment(n, r, det_x(n, x1, xn))
    return experiment.get_q_matrix()


def RA_Forsythe_non_uniform(n: int, r: int, tx: list[Rational]) -> list[list[Rational]]:
    experiment = ForsythePolynomialExperiment(n, r, tx)
    return experiment.get_q_matrix()


def RA_Forsythe_detx(n: int, x1: Rational, xn: Rational) -> list[Rational]:
    return det_x(n, x1, xn)


def RA_Forsythe_detx_real_to_virtual(n: int, x1: Rational, xn: Rational, z1: Rational, zn: Rational) \
        -> tuple[list[Rational], Rational, Rational]:
    return det_x_real_to_virtual(n, x1, xn, z1, zn)


def RA_Forsythe_polynomial(n: int, r: int, tx: list[Rational], ty: list[Rational], q_matrix: list[list[Rational]]) \
        -> tuple[list[Rational], list[Rational]]:
    experiment = ForsythePolynomialExperiment(n, r, tx, ty)
    thetas = experiment.get_thetas(q_matrix)
    var_thetas = experiment.get_var_thetas(q_matrix)
    return thetas, var_thetas


def RA_Forsythe_virtual_to_real(r: int, a: Rational, b: Rational, gamma: list[Rational],
                                q_matrix: list[list[Rational]]) -> tuple[list[Rational], list[Rational]]:
    experiment = ForsytheVirtualToRealExperiment(r, a, b, gamma)
    a_matrix = experiment.get_a_matrix()
    thetas = experiment.get_star_thetas(gamma, a_matrix)
    var_thetas = experiment.get_star_var_thetas(a_matrix, q_matrix)
    return thetas, var_thetas


class InvalidPrecisionException(Exception):
    def __str__(self):
        return 'Invalid precision!'


def RA_to_float(data: Any, precision: int = PRECISION):
    if precision < MIN_PRECISION or precision > MAX_PRECISION:
        raise InvalidPrecisionException()
    result = []
    is_list = data.__class__ == list
    sympy_classes = [Rational, Number, One, Zero, Integer, NegativeOne, Half]
    if data.__class__ in sympy_classes:
        return rational_to_float(data, precision)

    for elem in data:
        if elem.__class__ in sympy_classes:
            result.append(rational_to_float(elem, precision))
        elif elem.__class__ == list:
            result.append([RA_to_float(item, precision) for item in elem])
    if len(result) == 1:
        return result[0]

    if is_list:
        return result

    return tuple(result)
