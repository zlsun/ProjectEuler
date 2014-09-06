#-*- encoding: utf-8 -*-
"""
Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
"""

from utils import *

N = 1000
s = [0] * (N + 1)
for i in range(1, N / 2):
    for j in range(i, N / 2):
        ab2 = i ** 2 + j ** 2
        sq = int(ab2 ** 0.5)
        if sq ** 2 == ab2 and i + j + sq <= N:
            s[i + j + sq] += 1
print s.index(max(s))
# 840
