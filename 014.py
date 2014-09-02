#-*- encoding: utf-8 -*-
"""
Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from utils import *

@cache
def get_chain(n):
    if n == 1:
        return 1
    if n % 2:
        return get_chain(3 * n + 1) + 1
    else:
        return get_chain(n / 2) + 1

N = 1000000
longest = 0
for i in xrange(1, N + 1):
    l = get_chain(i)
    if l > longest:
        longest = l
        best = i
print best
# 837799
