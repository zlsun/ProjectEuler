#-*- encoding: utf-8 -*-
"""
Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

from utils import *

ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [None, 0, 6, 6, 5, 5, 5, 7, 6, 6]

@cache
def get_count(n):
    if n < 10:
        return ones[n]
    if n < 20:
        return teens[n - 10]
    if n < 100:
        return tens[n/10]+ones[n%10]
    if n < 1000:
        r = ones[n / 100] + 7
        if n % 100:
            r += 3 + get_count(n%100)
        return r
    if n==1000:
        return 3 + 8

print sum(map(get_count, xrange(1, 1001)))
# 21124
