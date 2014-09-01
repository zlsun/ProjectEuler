"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""

from utils import *

N = 600851475143
r = None
for p in get_primes(N ** 0.5):
    if N % p == 0:
        r = p
        N /= p
print r
# 6857
