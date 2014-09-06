#-*- encoding: utf-8 -*-
"""
Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from utils import *

is_curious = lambda n: sum(map(factorial, map(int, str(n)))) == n
print sum(filter(is_curious, xrange(3, 50000)))
# 40730
