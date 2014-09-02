"""
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
 a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.
"""

for a in range(1, 1000):
    for b in range(a + 1, 1000 - a + 1):
        for c in range(b + 1, 1000 - a - b + 1):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print a * b * c
                break
# 31875000
