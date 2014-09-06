#-*- encoding: utf-8 -*-
"""
Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from utils import *

# version 1
# s = set()
# for p in permutations('123456789'):
#     for i in range(1, 5):
#         for j in range(i + 1, 7):
#             if t2i(p[:i]) * t2i(p[i:j]) == t2i(p[j:]):
#                 s.add(t2i(p[j:]))
# print sum(s)

# version 2
pandigital = set()
for i in range(1, 10000):
    for j in range(i, int(10000/i)+1):
        if ''.join(sorted(list(str(i) + str(j) + str(i*j)))) == '123456789':
            pandigital.add(i*j)
print sum(pandigital)

# 45228
