#-*- encoding: utf-8 -*-
"""
Roman numerals

For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.
For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.
The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.
Find the number of characters saved by writing each of these in their minimal form.
Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""

from utils import *


def to_roman(i):
    s = ''
    while i >= 1000:
        s += 'M'
        i -= 1000
    for m, b, c, d in [(100, 'C', 'D', 'M'), (10, 'X', 'L', 'C'), (1, 'I', 'V', 'X')]:
        n = i / m
        if n < 4:
            s += b * n
        elif n == 4:
            s += b + c
        elif n < 9:
            s += c + b * (n - 5)
        elif n == 9:
            s += b + d
        i %= m
    return s


def from_roman(s):
    sp = {'I': 'VX', 'X': 'LC', 'C': 'DM'}
    c2i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = 0
    i = 0
    l = len(s)
    while i < l:
        c = s[i]
        if c in sp.keys() and i + 1 < l and s[i + 1] in sp[c]:
            r += c2i[s[i + 1]] - c2i[c]
            i += 1
        else:
            r += c2i[c]
        i += 1
    return r


L = file('./089_roman.txt').read().splitlines()
print sum(len(l) - len(to_roman(from_roman(l))) for l in L)
# 743
