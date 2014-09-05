#-*- encoding: utf-8 -*-
"""
Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:
14 = 2 ×715 = 3 ×5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2² ×7 ×23
645 = 3 ×5 ×43
646 = 2 ×17 ×19.
Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

from utils import *
from collections import deque

N = 4
i = 1
d = deque([0] * N)
while i < 200000:
    d.append(len(factors(i)))
    d.popleft()
    if all(j == N for j in d):
        print i - N + 1
        break
    i += 1
# 134043
