from regressionlib.experiments.constants import MAX_N, MIN_N
from regressionlib.experiments.abstract_experiment import AbstractExperiment, ExperimentException, InvalidValueException
from sympy import Rational


class UnivariateLinearRegressionExperimentException(ExperimentException):
    exception_codes = {
        100: '"N" value is not in range [' + str(MIN_N) + ', ' + str(MAX_N) + ']',
        300: 'X-matrix size does not match with "N" value',
        301: 'X-matrix size does not match with "M" value',
        400: 'Y-matrix size does not match with "N" value',
        500: 'Matrix is degenerated',
        600: 'Zero division',
        700: 'Input value is not a number'
    }


class UnivariateLinearRegressionExperiment(AbstractExperiment):
    def __init__(self, n: int, x: list[Rational], y: list[Rational]):
        self.n = n
        self.x = x
        self.y = y

        if n < MIN_N or n > MAX_N:
            raise UnivariateLinearRegressionExperimentException(100)

        if len(x) != n:
            raise UnivariateLinearRegressionExperimentException(300)

        if len(y) != n:
            raise UnivariateLinearRegressionExperimentException(400)

        try:
            self.check_for_numbers(x)
            self.check_for_numbers(y)
            self.check_for_int(n)
        except InvalidValueException:
            raise UnivariateLinearRegressionExperimentException(700)

    def __get_multiplied_sum(self, arr1: list[Rational], arr2: list[Rational]):
        multiplied_sum = 0
        for i in range(len(arr1)):
            multiplied_sum += arr1[i] * arr2[i]

        return multiplied_sum

    def __get_theta1(self) -> Rational:

        top_part = self.n * self.__get_multiplied_sum(self.x, self.y) - sum(self.x) * sum(self.y)
        bottom_part = self.n * self.__get_multiplied_sum(self.x, self.x) - sum(self.x) ** 2
        if bottom_part == 0:
            raise UnivariateLinearRegressionExperimentException(600)

        return top_part / bottom_part

    def __get_theta0(self, theta1) -> Rational:
        return (sum(self.y) - theta1 * sum(self.x)) / self.n

    def get_experiment_result(self) -> tuple[Rational, Rational]:
        theta1 = self.__get_theta1()
        theta0 = self.__get_theta0(theta1)
        return theta1, theta0
