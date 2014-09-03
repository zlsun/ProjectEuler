
import operator
from copy import deepcopy
from math import *
from itertools import *
from collections import defaultdict
from lru_cache import lru_cache
from lazy import *


def cache(func):
    pool = {}

    def wrapper(*args):
        if args in pool:
            return pool[args]
        else:
            pool[args] = func(*args)
            return pool[args]
    return wrapper


def groupcount(sq):
    ''' Accept a sequence sq, and count its elements by group '''
    d = defaultdict(int)  # default 0
    for each in sq:
        d[each] += 1
    return dict(d)


def fnchain(x, fs):
    for f in fs:
        x = f(x)
    return x


def is_prime(n):
    if n < 5:
        return n == 2 or n == 3
    return n % 2 and n % 3 and \
        all(n % (6 * k - 1) and n % (6 * k + 1)
            for k in range(1, int((n ** .5 + 1) / 6) + 1))


@lazylist
def sieve(n):
    n = int(n)
    n += 1
    isprime = sieve.isprime
    olen = len(isprime)
    if olen < n:
        isprime.extend([True] * max(olen / 2, n - olen))
        # print olen, len(isprime), n
        for i in xrange(2, int(n ** 0.5) + 1):
            if isprime[i]:
                for j in xrange(max(i * 2, (olen / i + 1) * i), n, i):
                    isprime[j] = False
    return islice(isprime, n)
sieve.isprime = [False, False]


@lazylist
def primes(n):
    ''' Generate primes <= n '''
    return (i for i, e in enumerate(sieve(n)) if e)


@lazylist
def factors(n):
    ''' Generate all prime factors of n '''
    f = 2
    while f * f <= n:
        while not n % f:
            yield f
            n /= f
        f += 1
    if n > 1:
        yield n

divisors = lambda n: [i for i in range(1, n + 1) if n % i == 0]


def divisors_num(n):
    """
    n = a^x*b^y*...*c^z
    d(n) = (x+1)*(y+1)*...*(z+1)
    """
    return product(x + 1 for x in groupcount(factors(n)).values())


def is_palindromic(s):
    # ~0 == -1, ~1 == -2
    return all(s[i] == s[~i] for i in range(len(s) / 2))


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

    def __iter__(self):
        def iter():
            for i in self.data:
                yield i
        return iter()

    def __str__(self):
        m = fnchain(self.data, [flatten, max, str, len])
        return '\n'.join(' '.join(('%%%dd' % m) % i for i in r) for r in self.data)

    def __add__(self, other):
        return Matrix(self.row, self.col).apply2(other, operator.add)

    def __sub__(self, other):
        return Matrix(self.row, self.col).apply2(other, operator.sub)

    def __mul__(self, other):
        return Matrix(self.row, self.col).apply2(other, operator.mul)

    def __div__(self, other):
        return Matrix(self.row, self.col).apply2(other, operator.div)

    def indexs(self):
        for i in range(self.row):
            for j in range(self.col):
                yield i, j

    def apply(self, f):
        for i in self.indexs():
            self[i] = f(self[i])
        return self

    def apply2(self, other, f):
        for i in self.indexs():
            self[i] = f(self[i], other[i])
        return self

    def move(self, *args):
        if len(args) == 2:
            v = args
        else:
            v = args[0]
        new = Matrix(self.row, self.col)
        for i in self.indexs():
            ni = v[0] + i[0], v[1] + i[1]
            if any(x < 0 for x in ni):
                continue
            new[ni] = self[i]
        return new

dire4 = [(0, -1), (0, 1), (-1, 0), (1, 0)]
dire8 = dire4 + [(-1, -1), (1, -1), (-1, 1), (1, 1)]

if __name__ == '__main__':
    print is_prime(2), is_prime(3), is_prime(4)
    print sieve(10)
    print primes(2), primes(20)
    print factors(8)
    print divisors(8), divisors(220)
    print divisors_num(13), divisors_num(8)
    print is_palindromic('101'), is_palindromic('110')
    print product(range(1, 4))
    print gcd(2, 8)
    print lcm(2, 3)
    print factorial(4)
    print square(4)
    m = Matrix([[1, 2], [3, 4]])
    print '-'.join(map(str, m))
    print m.move(1, 1)
    print m.move(-1, -1)
