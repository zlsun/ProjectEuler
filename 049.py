#-*- encoding: utf-8 -*-
"""
Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from utils import *

s = sieve(10000)
for i in primes(10000):
    if i > 1000 and i != 1487:
        o = filter(lambda n: s[n], map(t2i, permutations(str(i))))
        oo = filter(bool, map(lambda n: n - i, o))
        ooo = [[i + n, i + n * 2] for n in oo if oo.count(n * 2) and n > 0]
        if ooo:
            ii = ooo[0]
            print i, ii, ii[1] - ii[0]
            print ''.join(map(str, [i] + ii))
# 296962999629
