#-*- encoding: utf-8 -*-
"""
Cubic permutations

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.
"""

from collections import defaultdict

from utils import *

m = defaultdict(int)
n = defaultdict(int)
h = lambda n: ''.join(str(c) for c in sorted(str(n)))
i = 1
while 1:
    c = i ** 3
    hc = h(c)
    m[hc] += 1
    if n[hc] == 0 or c < n[hc]:
        n[hc] = c
    if m[hc] == 5:
        print n[hc]
        break
    i += 1

# 127035954683
