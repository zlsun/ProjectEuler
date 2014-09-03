#-*- encoding: utf-8 -*-
"""
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

from utils import *

n = 0
print max(i * j for i in range(100, 1000) for j in range(100, 1000) if is_palindromic(str(i * j)))
# 906609
