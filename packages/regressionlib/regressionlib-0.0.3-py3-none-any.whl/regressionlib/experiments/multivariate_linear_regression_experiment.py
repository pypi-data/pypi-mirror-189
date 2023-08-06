from regressionlib.experiments.constants import MAX_M, MAX_N, MIN_M, MIN_N
from regressionlib.experiments.abstract_experiment import AbstractExperiment, ExperimentException, InvalidValueException
from regressionlib.experiments.least_squares import least_squares, DegeneratedMatrixException
from sympy import Rational


class MultivariateLinearRegressionExperimentException(ExperimentException):
    exception_codes = {
        100: '"N" value is not in range [' + str(MIN_N) + ', ' + str(MAX_N) + ']',
        200: '"M" value is not in range [' + str(MIN_M) + ', ' + str(MAX_M) + ']',
        300: 'X-matrix size does not match with "N" value',
        301: 'X-matrix size does not match with "M" value',
        400: 'Y-matrix size does not match with "N" value',
        500: 'Matrix is degenerated',
        700: 'Input value is not a number'
    }


class MultivariateLinearRegressionExperiment(AbstractExperiment):
    def __init__(self, n: int, m: int, x: list[list[Rational]], y: list[Rational]):
        self.n = n
        self.m = m
        self.x = x
        self.y = y

        if n < MIN_N or n > MAX_N:
            raise MultivariateLinearRegressionExperimentException(100)
        if m < MIN_M or m > MAX_M:
            raise MultivariateLinearRegressionExperimentException(200)
        if len(x) != n:
            raise MultivariateLinearRegressionExperimentException(300)
        if len(x[0]) != m:
            raise MultivariateLinearRegressionExperimentException(301)
        if len(y) != n:
            raise MultivariateLinearRegressionExperimentException(400)
        try:
            [self.check_for_numbers(line) for line in x]
            self.check_for_numbers(y)
            self.check_for_int(n)
            self.check_for_int(m)
        except InvalidValueException:
            raise MultivariateLinearRegressionExperimentException(700)

    def __find_a_matrix(self) -> list[list[Rational]]:
        return [[Rational(1)] + xi for xi in self.x]

    def get_experiment_result(self) -> list[Rational]:
        a_matrix = self.__find_a_matrix()
        try:
            matrix = least_squares(a_matrix, [[yi] for yi in self.y])
            return [line[0] for line in matrix]
        except DegeneratedMatrixException:
            raise MultivariateLinearRegressionExperimentException(500)
