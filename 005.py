#-*- encoding: utf-8 -*-
"""
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from utils import *

N = 20
print reduce(lcm, range(1, N + 1))
# 232792560
