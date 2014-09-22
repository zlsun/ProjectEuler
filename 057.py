#-*- encoding: utf-8 -*-
"""
Square root convergents

It is possible to show that the square root of two can be expressed as an infinite continued fraction.
√2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""

from utils import *


def gen_root():
    num, den = 1, 1
    while 1:
        num, den = num + 2 * den, num + den
        l = gcd(num, den)
        num /= l
        den /= l
        # print num, den, num * 1. / den
        yield num, den
print sum(len(str(num)) > len(str(den)) for num, den in islice(gen_root(), 1000))
# 153
