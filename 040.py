#-*- encoding: utf-8 -*-
"""
Champernowne's constant

An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

from utils import *

s = "0"
i = 1
while len(s) <= 1000000:
    s += str(i)
    i += 1
print product(int(s[10 ** i]) for i in range(7))
# 210
