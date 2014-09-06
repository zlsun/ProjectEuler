#-*- encoding: utf-8 -*-
"""
Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from utils import *

N = 10000
s = sieve(N)
composites = (i for i, e in enumerate(s) if i % 2 and not e)
composites.next()
is_twice_square = (lambda n: n > 0 and n % 2 == 0 and int((n / 2) ** 0.5) ** 2 == n / 2)
ok = (lambda n: any(is_twice_square(n - i) for i in range(n - 1, 0, -1) if s[i]))
print dropwhile(ok, composites).next()
# 5777
