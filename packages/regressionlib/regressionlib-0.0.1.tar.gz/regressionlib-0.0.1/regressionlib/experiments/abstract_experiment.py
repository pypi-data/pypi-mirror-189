from typing import Any
from sympy import Rational, Integer
from sympy.core.numbers import One, Zero, Number, NegativeOne, Half


class InvalidValueException(Exception):
    pass


class ExperimentException(Exception):
    exception_codes: dict[int, str] = {}

    def __init__(self, code: int):
        message = 'Error ' + str(code) + ': ' + self.exception_codes.get(code)
        super().__init__(message)


class AbstractExperiment:
    def get_experiment_result(self) -> Any:
        pass

    def check_for_numbers(self, values: list[Rational]):
        sympy_classes = [Rational, Number, One, Zero, Integer, NegativeOne, Half]

        for item in values:
            if item.__class__ not in sympy_classes:
                raise InvalidValueException()

    def check_for_int(self, value: int):
        if value.__class__ != int:
            raise InvalidValueException()
