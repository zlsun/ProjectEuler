#-*- encoding: utf-8 -*-
"""
Digit factorial chains

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145
Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872
It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)
Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

from utils import *

sum_of_factorial = lambda n: sum(map(factorial, digits(n)))

@no_loop_cache(0)
def get_chain(n):
    s = sum_of_factorial(n)
    if s == n:
        return 0
    else:
        return get_chain(s) + 1

print len(filter(lambda x: x == 60, map(get_chain, xrange(10 ** 6))))

# 402
