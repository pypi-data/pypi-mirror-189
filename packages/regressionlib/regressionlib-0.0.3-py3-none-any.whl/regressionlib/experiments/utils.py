from sympy import Rational, Float
from math import floor


def rational_to_float(num: Rational, precision: int) -> Float:
    int_val = floor(abs(num.numerator / num.denominator))

    zeros_after_comma = 0
    temp = num

    if temp != 0:
        while abs(temp.numerator) < abs(temp.denominator):
            temp *= 10
            zeros_after_comma += 1

    new_precision = precision + (len(str(int_val)) if int_val != 0 else (1 - zeros_after_comma))
    return num.evalf(new_precision)
