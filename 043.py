#-*- encoding: utf-8 -*-
"""
Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from utils import *

# version 1
r = zip(range(1, 8), [2, 3, 5, 7, 11, 13, 17])
valid = lambda n: all(int(''.join(n[i:i + 3])) % p == 0 for i, p in r)
numbers = (int(''.join(i)) for i in permutations('0123456789') if valid(i))
# print sum(numbers)

# version 2
nums = [str(i).zfill(3)
        for i in xrange(0, 1000, 17) if len(set(str(i).zfill(3))) == 3]
print nums[:20]
for i in [13, 11, 7, 5, 3, 2, 1]:
    tmp = []
    for j in nums:
        for k in '0123456789':
            if not k in j and int(k + j[:2]) % i == 0:
                    tmp.append(k + j)
    nums = tmp
print sum(map(int, nums))

# 16695334890
