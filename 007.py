"""
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

from utils import *

N = 10001
print primes(N * 100)[N - 1]
# 104743
