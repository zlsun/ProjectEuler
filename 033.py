#-*- encoding: utf-8 -*-
"""
Digit canceling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from __future__ import division
from utils import *

ii, jj = 1, 1
for i in range(10, 99):
    for j in range(10, 99):
        i1, i2 = divmod(i, 10)
        j1, j2 = divmod(j, 10)
        if j2 == 0:
            continue
        if i1 != i2 and i2 == j1 and i / j == i1 / j2:
            ii *= i
            jj *= j
print int(jj / gcd(ii, jj))
# 100
