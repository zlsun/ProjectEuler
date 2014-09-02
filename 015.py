#-*- encoding: utf-8 -*-
"""
Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
             ▁ ▁     ▁ _     ▁ _     _ _      _ _      _ _ 
            |_|_┃   |_┃▁|   |_┃_|   ┃▁|▁|    ┃▁|_|    ┃_|_|
            |_|_┃   |_|_┃   |_┃▁|   |_|_┃    |_┃▁|    ┃▁|▁|

How many such routes are there through a 20×20 grid?
"""

from utils import *

@cache
def get(sel, left):
    if left == 0:
        return 1
    return sum(get(i, left - 1) for i in range(1, sel + 1))

N = 20
print get(N + 1, N)
# 137846528820
