#-*- encoding: utf-8 -*-
"""
Coded triangle numbers

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

from utils import *


triangle = lambda n: (lambda s: s * (s + 1) == n * 2)(int((n * 2) ** 0.5))
words = eval("[%s]" % file('042_words.txt').read())
values = (sum(ord(c) - ord('A') + 1 for c in w) for w in words)
triwords = filter(triangle, values)
print len(triwords)
# 162
