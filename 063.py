#-*- encoding: utf-8 -*-
"""
Powerful digit counts

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
How many n-digit positive integers exist which are also an nth power?
"""

from utils import *

print len([(i, n) for n in range(1, 200) for i in range(1, 10) if len(str(i ** n)) == n])
# 49
