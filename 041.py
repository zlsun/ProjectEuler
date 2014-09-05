#-*- encoding: utf-8 -*-
"""
Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""

from utils import *

# version 1
def pandigital(n):
    s = str(n)
    return sorted(map(int, s)) == range(1, len(s) + 1)
# print filter(pandigital, primes(10000000))[-1]

# version 2
print ''.join(filter(lambda t: is_prime(int(''.join(t))), permutations('1234567'))[-1])

# 7652413
