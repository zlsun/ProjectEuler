#-*- encoding: utf-8 -*-
"""
Arranged probability

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""

from utils import *

n = 10**12
# i=1
while True:#i<100:
    nn = n*(n-1)/2
    sq = int(nn**0.5)
    # print sq+1,n,sq*(sq+1),nn, cmp(sq*(sq+1),nn)
    if sq*(sq+1)==nn:
        print sq+1
        break
    n+=1
    # i+=1
# 
