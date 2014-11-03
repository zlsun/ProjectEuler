#-*- encoding: utf-8 -*-
"""
Square root digital expansion

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.
The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""

from decimal import *

from utils import *

getcontext().prec = 102
p = 10 ** 100


def sum_of_sqrt_decimal(s):
    q = Decimal(s).sqrt()
    if q % 1 == 0:
        return 0
    return sum(map(int, str(q * p)[:100]))

print sum(sum_of_sqrt_decimal(str(i)) for i in range(1, 101))

# 40886
