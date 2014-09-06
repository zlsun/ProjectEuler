#-*- encoding: utf-8 -*-
"""
Circular primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""

from utils import *

circular_prime = lambda p: all(is_prime(int(i)) for i in circular(str(p)))
print len(filter(circular_prime, primes(1000000)))
# 55
