#-*- encoding: utf-8 -*-
"""
Counting summations

It is possible to write five as a sum in exactly six different ways:
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
How many different ways can one hundred be written as a sum of at least two positive integers?
"""

from utils import *

@cache
def solve(n, m):
    if n < 0:
        return 0
    if n == 0:
        return 1
    s = 0
    for i in range(1, m + 1):
        s += solve(n - i, min(i, m))
    return s

print solve(100, 99)
# 190569291
