
import operator
from copy import deepcopy
from itertools import islice
from math import *
from lru_cache import lru_cache


def cache(func):
    pool = {}
    def wrapper(*args):
        if args in pool:
            return pool[args]
        else:
            pool[args] = func(*args)
            return pool[args]
    return wrapper


def is_prime(n):
    for i in xrange(2, int(n ** 0.5) + 1):
        if n % i:
            return False
    return True


def get_primes_map(n):
    n += 1
    isprime = get_primes_map.isprime
    olen = len(isprime)
    if olen < n:
        isprime.extend([True] * max(olen / 2, n - olen))
        # print olen, len(isprime), n
        for i in xrange(2, n):
            if isprime[i]:
                for j in xrange(max(i * 2, (olen / i + 1) * i), n, i):
                    isprime[j] = False
    return islice(isprime, n)
get_primes_map.isprime = [False, False]


def get_primes(n):
    """ get primes <= n """
    return [i for i, e in enumerate(get_primes_map(n)) if e]


def factors(n):
    L = []
    for p in get_primes(n):
        while n % p == 0:
            L.append(p)
            n /= p
        if n == 1:
            break
    return L

divisors = lambda n: [i for i in range(1, n + 1) if n % i == 0]


def divisors_num(n):
    """
    n = product(p[n]^v[n])
    d(n) = sum(v[n])
    """
    r = 1
    l = len(divisors_num.primes)
    # if n > 598 then
    # (n/log(n))*(1 + 0.992/log(n)) < pi(n) < (n/log(n))*(1 + 1.2762/log(n))
    # The upper bound holds for all n > 1. This gives a tight bound for larger n.
    # Note n/log(n) < pi(n) for n > 10.
    if n > 1 and n ** 0.5 > l: #(n / log(n)) * (1 + 1.2762 / log(n)) > l:
        divisors_num.primes = get_primes(n)
    for p in divisors_num.primes:
        v = 0
        while n % p == 0:
            v += 1
            n /= p
        r *= (v + 1)
        if n == 1:
            break
    return r
divisors_num.primes = []


def is_palindromic(n):
    s = str(n)
    l = len(s)
    for i in range(l / 2):
        if s[i] != s[l - i - 1]:
            return False
    return True


def gcd(a, b):
    while b > 0:
        b, a = a % b, b
    return a


lcm = lambda a, b: a / gcd(a, b) * b
product = lambda L, init=1: reduce(operator.mul, L, init)
factorial = lambda n: product(xrange(1, n + 1))
square = lambda n: n * n
flatten = lambda m: sum(m, [])
transpose = lambda m: map(list, zip(*transpose))


class Matrix(object):

    def __init__(self, *args):
        if len(args) == 1:
            m = args[0]
            self.row, self.col = len(m), len(m[0])
            self.data = deepcopy(m)
        elif len(args) == 2:
            self.row, self.col = args
            self.data = [[0] * self.col for _ in range(self.row)]

    def __getitem__(self, i):
        try:
            if type(i) == int:
                return self.data[i]
            elif type(i) == tuple:
                r, c = i
                return self.data[r][c]
        except IndexError:
            pass

    def __setitem__(self, i, value):
        try:
            if type(i) == int:
                self.data[i] = value
            elif type(i) == tuple:
                r, c = i
                self.data[r][c] = value
        except IndexError:
            pass

    def __str__(self):
        m = len(str(max(sum(self.data, []))))
        return '\n'.join(' '.join(('%%%dd' % m) % i for i in r) for r in self.data)

    def __add__(self, other):
        new = Matrix(self.row, self.col)
        for i in self.indexs():
            new[i] = self[i] + other[i]
        return new

    def __sub__(self, other):
        new = Matrix(self.row, self.col)
        for i in self.indexs():
            new[i] = self[i] - other[i]
        return new

    def __mul__(self, other):
        new = Matrix(self.row, self.col)
        for i in self.indexs():
            new[i] = self[i] * other[i]
        return new

    def __div__(self, other):
        new = Matrix(self.row, self.col)
        for i in self.indexs():
            new[i] = self[i] / other[i]
        return new

    def indexs(self):
        for i in range(self.row):
            for j in range(self.col):
                yield i, j

    def apply(self, f):
        for i in self.indexs():
            self[i] = f(self[i])

    def move(self, *args):
        if len(args) == 2:
            v = args
        else:
            v = args[0]
        new = Matrix(self.row, self.col)
        for i in self.indexs():
            ni = v[0] + i[0]
            nj = v[1] + i[1]
            if ni < 0 or nj < 0:
                continue
            new[ni, nj] = self[i]
        return new

dire4 = [(0, -1), (0, 1), (-1, 0), (1, 0)]
dire8 = dire4 + [(-1, -1), (1, -1), (-1, 1), (1, 1)]

if __name__ == '__main__':
    print is_prime(2), is_prime(3), is_prime(4)
    print list(get_primes_map(10))
    print get_primes(2), get_primes(20)
    print factors(8)
    print divisors(8)
    print divisors_num(13), divisors_num(8)
    print is_palindromic(101), is_palindromic(110)
    print product(range(1, 4))
    print gcd(2, 8)
    print lcm(2, 3)
    print factorial(4)
    print square(4)
    print Matrix([[11, 2], [3, 4]]).move(1, 1)
    print Matrix([[11, 2], [3, 4]]).move(-1, -1)
