#-*- encoding: utf-8 -*-
"""
Permuted multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

from utils import *

i = 1
while 1:
    s = set(str(i))
    if all(set(str(j * i)) == s for j in range(2, 7)):
        break
    i += 1
print i
# 142857
