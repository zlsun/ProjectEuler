
import operator
import fn
from copy import deepcopy
from math import *
from itertools import *
from functools import *
from collections import defaultdict
from lazy import *


def trace(func):
    def wrapper(*args, **kwds):
        indent = ' ' * trace.level
        print "Log: %s%s(%s)" % (indent, func.__name__,
                                 ', '.join(map(str, args) + ['%s=%s' % i for i in kwds.items()]))
        trace.level += 1
        result = func(*args)
        trace.level -= 1
        print "Log: %s-> %s" % (indent, result)
        return result
    return wrapper
trace.level = 0


def cache(func):
    cached = {}

    def wrapper(*args):
        if args in cached:
            return cached[args]
        else:
            cached[args] = func(*args)
            return cached[args]
    return wrapper


def no_loop_cache(n):
    def cache(func):
        cached = {}

        def wrapper(*args):
            if args in cached:
                if cached[args] == None:
                    cached[args] = 0
                return cached[args]
            else:
                cached[args] = None
                cached[args] = func(*args)
                return cached[args]
        return wrapper
    return cache


def groupcount(sq):
    ''' Accept a sequence sq, and count its elements by group '''
    d = defaultdict(int)  # default 0
    for each in sq:
        d[each] += 1
    return dict(d)


def fnchain(x, fs):
    return reduce(lambda x, f: f(x), fs, x)


@lazylist
def fib(n=None):
    a, b = 1, 1
    if n == None:
        while True:
            yield a
            b, a = a + b, b
    else:
        while a <= n:
            yield a
            b, a = a + b, b


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
@cache
def primes(n):
    ''' Generate primes <= n '''
    return (i for i, e in enumerate(sieve(n)) if e)


@lazylist
def factors(n):
    ''' Generate all prime factors of n '''
    f = 2
    while f * f <= n:
        v = 0
        while not n % f:
            v += 1
            n /= f
        if v:
            yield f, v
        f += 1
    if n > 1:
        yield n, 1


@lazylist
def divisors(n):
    for i in xrange(1, n / 2 + 1):
        if n % i == 0:
            yield i
    yield n


def divisors_num(n):
    """
    n = a^x * b^y * ... * c^z
    divisors_num(n) = (x+1)*(y+1)*...*(z+1)
    See: http://en.wikipedia.org/wiki/Divisor
    """
    return product(p + 1 for _, p in factors(n))


def divisors_sum(n):
    """
    n = a^x * b^y * ... * c^z
    divisors_sum(n) = (a^(x+1)-1)/(a-1) * ...
    See: http://en.wikipedia.org/wiki/Divisor_function
    """
    return product(x + 1 if p == 1 else ((x ** (p + 1) - 1) / (x - 1)) for x, p in factors(n))


def is_palindromic(s):
    # ~0 == -1, ~1 == -2
    return all(s[i] == s[~i] for i in range(len(s) / 2))


def gcd(a, b):
    while b > 0:
        b, a = a % b, b
    return a


@lazylist
def circular(s):
    return (s[i:] + s[:i] for i in range(len(s)))

t2s = lambda t: ''.join(t)
t2i = lambda t: int(t2s(t))
permutations = lazylist(permutations)
combinations = lazylist(combinations)

lcm = lambda a, b: a / gcd(a, b) * b
product = lambda L, init=1: reduce(operator.mul, L, init)
factorial = lambda n: product(xrange(1, n + 1))
P = lambda n, m: factorial(n) / factorial(n - m)
C = lambda n, m: P(n, m) / factorial(m)
square = lambda n: n * n
flatten = lambda m: sum(m, [])
transpose = lambda m: map(list, zip(*m))
digits = lambda n: map(int, str(n))

vadd = lambda a, b: tuple(i + j for i, j in zip(a, b))
vsub = lambda a, b: tuple(i - j for i, j in zip(a, b))
vmul = lambda v, i: tuple(e * i for e in v)
vdiv = lambda v, i: tuple(e / i for e in v)


class Matrix(object):

    def __init__(self, *args):
        if len(args) == 1:
            m = args[0]
            self.row, self.col = len(m), len(m[0])
            self.data = deepcopy(m)
        elif len(args) == 2:
            self.row, self.col = args
            self.data = [[0] * self.col for _ in range(self.row)]

    def __getitem__(self, idx):
        try:
            if type(idx) == int:
                return self.data[idx]
            elif type(idx) == tuple:
                r, c = idx
                return self.data[r][c]
        except IndexError:
            pass

    def __setitem__(self, idx, value):
        if isinstance(idx, int):
            self.data[idx] = value
        elif isinstance(idx, (tuple, list)):
            r, c = idx
            self.data[r][c] = value

    def __iter__(self):
        def iter():
            for i in self.data:
                yield i
        return iter()

    def __str__(self):
        m = fnchain(self.data, [flatten, max, str, len])
        return '\n'.join(' '.join(('%%%dd' % m) % i for i in r) for r in self.data)

    def __add__(self, other):
        return Matrix(self.data).apply2(other, operator.add)

    def __sub__(self, other):
        return Matrix(self.data).apply2(other, operator.sub)

    def __mul__(self, other):
        return Matrix(self.data).apply2(other, operator.mul)

    def __div__(self, other):
        return Matrix(self.data).apply2(other, operator.div)

    def size(self):
        return (self.row, self.col)

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
        v = args[0] if len(args) == 1 else args
        new = Matrix(self.row, self.col)
        for i in self.indexs():
            ni = vadd(i, v)
            if any(x < 0 or x >= y for x, y in zip(ni, self.size())):
                continue
            new[ni] = self[i]
        return new

    def transpose(self):
        return Matrix(transpose(self))


dire4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dire8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

if __name__ == '__main__':
    print is_prime(2), is_prime(3), is_prime(4)
    print sieve(10)
    print primes(2), primes(20)
    print factors(8)
    print divisors(0), divisors(1), divisors(8), divisors(220), divisors(72)
    print divisors_num(0), divisors_num(1), divisors_num(13), divisors_num(8), divisors_num(72)
    print divisors_sum(0), divisors_sum(1), divisors_sum(13), divisors_sum(8), divisors_sum(72)
    print is_palindromic('101'), is_palindromic('110')
    print permutations('012')
    print circular('197')
    print product(range(1, 4))
    print gcd(2, 8)
    print lcm(2, 3)
    print factorial(4)
    print square(4)
    m = Matrix([[1, 2], [3, 4]])
    print '-'.join(map(str, m))
    print m.move(1, 1)
    print m.move(-1, -1)
    print (m * m).transpose()
    print flatten(m)
