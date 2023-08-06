from regressionlib.experiments.constants import MAX_N, MAX_R, MIN_N, MIN_R
from regressionlib.experiments.abstract_experiment import AbstractExperiment, ExperimentException, InvalidValueException
from sympy import Rational

from regressionlib.experiments.least_squares import least_squares, DegeneratedMatrixException


class UnivariatePolynomialRegressionExperimentException(ExperimentException):
    exception_codes = {
        100: '"N" value is not in range [' + str(MIN_N) + ', ' + str(MAX_N) + ']',
        101: '"N" value is smaller than "R" value',
        200: '"R" value is not in range [' + str(MIN_R) + ', ' + str(MAX_R) + ']',
        300: 'X-matrix size does not match with "N" value',
        400: 'Y-matrix size does not match with "N" value',
        500: 'Matrix is degenerated',
        700: 'Input value is not a number'
    }


class UnivariatePolynomialRegressionExperiment(AbstractExperiment):
    def __init__(self, n: int, r: int, tx: list[Rational], ty: list[Rational]):
        self.n = n
        self.r = r
        self.tx = tx
        self.ty = ty

        if n < MIN_N or n > MAX_N:
            raise UnivariatePolynomialRegressionExperimentException(100)
        if n < r:
            raise UnivariatePolynomialRegressionExperimentException(101)
        if r < MIN_R or r > MAX_R:
            raise UnivariatePolynomialRegressionExperimentException(200)
        if len(tx) != n:
            raise UnivariatePolynomialRegressionExperimentException(300)
        if len(ty) != n:
            raise UnivariatePolynomialRegressionExperimentException(400)
        try:
            self.check_for_numbers(tx)
            self.check_for_numbers(ty)
            self.check_for_int(n)
            self.check_for_int(r)
        except InvalidValueException:
            raise UnivariatePolynomialRegressionExperimentException(700)

    def __get_a_matrix(self) -> list[list[Rational]]:
        return [[self.tx[i] ** j for j in range(self.r + 1)] for i in range(self.n)]

    def get_experiment_result(self) -> list[Rational]:
        try:
            matrix = least_squares(self.__get_a_matrix(), [[y] for y in self.ty])
            return [line[0] for line in matrix]

        except DegeneratedMatrixException:
            raise UnivariatePolynomialRegressionExperimentException(500)
