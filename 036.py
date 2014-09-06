#-*- encoding: utf-8 -*-
"""
Double-base palindromes

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from utils import *

print sum(i for i in xrange(1,1000000) if is_palindromic(str(i)) and is_palindromic(bin(i)[2:]))
# 872187
