#-*- encoding: utf-8 -*-
"""
Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from utils import *

N = 1000000
s = sieve(N)
print sum(p for p in primes(N) if p > 10 and all(s[int(i)]
            for i in (lambda s:
                flatten([s[:i], s[i:]] for i in range(1, len(s)))
            )(str(p))
         ))
# 748317
