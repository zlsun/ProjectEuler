
def is_prime(n):
    for i in xrange(2, int(n ** 0.5) + 1):
        if n % i:
            return False
    return True


def get_primes_map(n):
    n = int(n)
    isprime = [True for _ in xrange(n)]
    isprime[0] = isprime[1] = False
    for i in xrange(2, n):
        if isprime[i]:
            for j in xrange(i * 2, n, i):
                isprime[j] = False
    return isprime


def get_primes(n):
    return [i for i, e in enumerate(get_primes_map(n)) if e]


def factors(n):
    L = []
    for p in get_primes(n):
        while n % p == 0:
            L.append(p)
            n /= p
            if p == 1:
                break
    return L


def is_palindromic(n):
    s = str(n)
    l = len(s)
    for i in range(l / 2):
        if s[i] != s[l - i - 1]:
            return False
    return True


if __name__ == '__main__':
    print is_prime(2), is_prime(3), is_prime(4)
    print get_primes_map(10)
    print get_primes(20)
    print factors(8)
    print is_palindromic(101), is_palindromic(110)
