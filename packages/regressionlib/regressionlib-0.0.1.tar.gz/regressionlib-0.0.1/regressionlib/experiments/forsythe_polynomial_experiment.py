from regressionlib.experiments.constants import MAX_N, MAX_R, MIN_N, MIN_R
from sympy import Poly, Rational
from sympy.abc import x
from regressionlib.experiments.abstract_experiment import AbstractExperiment, ExperimentException, InvalidValueException


class ForsythePolynomialExperimentException(ExperimentException):
    exception_codes = {
        100: '"N" value is not in range [' + str(MIN_N) + ', ' + str(MAX_N) + ']',
        101: '"N" value is smaller than "R" value',
        200: '"R" value is not in range [' + str(MIN_R) + ', ' + str(MAX_R) + ']',
        300: 'X-matrix size does not match with "N" value',
        400: 'Y-matrix size does not match with "N" value',
        500: 'Task is degenerated as Xi=0',
        700: 'Input value is not a number'
    }


def det_x(n: int, x1: Rational, xn: Rational) -> list[Rational]:
    d = (xn - x1) / (n - 1)
    res = [x1 + i * d for i in range(n)]
    return res


class ForsythePolynomialExperiment(AbstractExperiment):
    def __init__(self, n: int, r: int, tx: list[Rational], ty: list[Rational] = None):
        self.n = n
        self.r = r
        self.tx = tx
        self.ty = ty

        if n < MIN_N or n > MAX_N:
            raise ForsythePolynomialExperimentException(100)
        if r < MIN_R or r > MAX_R:
            raise ForsythePolynomialExperimentException(200)
        if n < r:
            raise ForsythePolynomialExperimentException(101)
        if len(self.tx) != n:
            raise ForsythePolynomialExperimentException(300)
        if self.ty is not None and len(self.ty) != n:
            raise ForsythePolynomialExperimentException(400)
        try:
            self.check_for_numbers(tx)
            if ty is not None:
                self.check_for_numbers(ty)
            self.check_for_int(n)
            self.check_for_int(r)
        except InvalidValueException:
            raise ForsythePolynomialExperimentException(700)
        tx_sum = 0
        for xi in tx:
            tx_sum += xi

        self.xs = Rational(tx_sum / len(self.tx))

        self.cache: dict[int, Poly] = {}
        self.cache_a: dict[int, Rational] = {}
        self.cache_b: dict[int, Rational] = {}
        self.cache_q_eval: dict[int, dict[Rational, Rational]] = {}
        for ri in range(r + 1):
            self.cache_q_eval[ri] = {}

    def eval_q_polynomial(self, num: int, xi: Rational) -> Rational:
        result = self.cache_q_eval[num].get(xi)
        if result is not None:
            return result
        result = self.__get_q(num).eval(xi)
        self.cache_q_eval[num][xi] = result
        return result

    def get_q_matrix(self):
        return self.convert_polynomials_to_matrix(self.get_q_polynomials())

    def get_coefficients_evaluation(self, q_matrix):
        thetas = self.get_thetas(q_matrix)
        var_thetas = self.get_var_thetas(q_matrix)
        return thetas, var_thetas

    def get_q_polynomials(self) -> list[Poly]:
        return [self.__get_q(i) for i in range(self.r + 1)]

    def convert_polynomials_to_matrix(self, q_polynomials: list[Poly]) -> list[list[Rational]]:
        q_matrix = [[Rational(0) for _ in range(self.r + 1)] for _ in range(self.r + 1)]
        for i in range(len(q_polynomials)):
            exp = q_polynomials[i].as_expr()
            for j in range(self.r + 1):
                q_matrix[j][i] = exp.coeff(x, j)

        return q_matrix

    def convert_matrix_to_polynomials(self, q_matrix: list[list[Rational]]) -> list[Poly]:
        q_polynomials = []
        for i in range(self.r + 1):
            exp = 0
            for j in range(self.r + 1):
                exp += x ** j * q_matrix[j][i]
            q_polynomials.append(Poly(exp, x))
        return q_polynomials

    def __get_q(self, num: int) -> Poly:
        result = self.cache.get(num)
        if result is not None:
            return result

        if num == 0:
            result = Poly(Rational(1 / (self.n ** (1 / 2))), x)
        elif num == 1:
            bottom_sum = Rational(0)
            for xi in self.tx:
                bottom_sum += (xi - self.xs) ** 2
            bottom_part = Rational(bottom_sum ** 0.5)

            result = Poly(x / bottom_part - self.xs / bottom_part, x)
        else:
            a = self.__get_a(num)
            b = self.__get_b(num)
            l = self.__get_l(num)
            previous_q = self.__get_q(num - 1)
            pre_previous_q = self.__get_q(num - 2)
            first_sub = Poly(x, x) * previous_q
            second_sub = previous_q * a
            third_sub = pre_previous_q * b
            curr_l = l
            result = ((first_sub - second_sub - third_sub) / curr_l).as_poly()
        self.cache[num] = result
        return result

    def __get_a(self, num: int) -> Rational:
        res = self.cache_a.get(num)
        if res is not None:
            return res

        res = sum([xi * (self.eval_q_polynomial(num - 1, xi) ** 2) for xi in self.tx])
        self.cache_a[num] = res
        return res

    def __get_b(self, num: int) -> Rational:
        res = self.cache_b.get(num)
        if res is not None:
            return res
        res = sum([xi * self.eval_q_polynomial(num - 1, xi) * self.eval_q_polynomial(num - 2, xi)
                   for
                   xi
                   in self.tx])

        self.cache_b[num] = res
        return res

    def __get_l(self, num: int) -> Rational:
        arr = [(xi * self.eval_q_polynomial(num - 1, xi) -
                self.__get_a(num) * self.eval_q_polynomial(num - 1, xi) -
                self.__get_b(num) * self.eval_q_polynomial(num - 2, xi)) ** 2
               for xi in self.tx]
        return Rational(sum(arr) ** 0.5)

    def get_w(self, q_polynomials: list[Poly]) -> list[Rational]:
        w = []
        for j in range(self.r + 1):
            curr_q = q_polynomials[j]

            curr_sum = Rational(0)
            for i in range(self.n):
                curr_sum += curr_q.eval(self.tx[i]) * self.ty[i]
            w.append(curr_sum)

        return w

    def get_thetas(self, q_matrix: list[list[Rational]]) -> list[Rational]:
        q_polynomials = self.convert_matrix_to_polynomials(q_matrix)
        w = self.get_w(q_polynomials)
        return [
            sum([w[i] * q_matrix[j][i] for i in range(self.r + 1)]) for j in range(self.r + 1)
        ]

    def get_var_thetas(self, q_matrix: list[list[Rational]]) -> list[Rational]:
        return [
            sum([q_matrix[j][i] ** 2 for i in range(self.r + 1)]) for j in range(self.r + 1)
        ]
