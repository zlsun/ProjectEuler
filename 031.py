#-*- encoding: utf-8 -*-
"""
Coin sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

from utils import *

ps = [200, 100, 50, 20, 10, 5, 2, 1]

def calc(remind, ps,a=1):
    if len(ps) == 1:
        return remind % ps[0] == 0
    s = 0
    for i in range(remind / ps[0] + 1):
        s += calc(remind - ps[0] * i, ps[1:])
    return s

print calc(200, ps)
# 73682
