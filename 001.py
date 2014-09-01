"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

N = 1000
mod = lambda l, n: [x for x in range(n) if any(x % a == 0 for a in l)]
print sum(mod([3, 5], N))
# 233168
