from math import factorial
from collections import Counter
from fractions import gcd #This does not work in Python 3 however Google's foobar uses Python 2


def cycle_count(c, n):
    cc = factorial(n)
    for a, b in Counter(c).items():
        cc //= (a**b)*factorial(b)
    return cc


def cycle_partitions(n, i=1):
    yield [n]
    for i in range(i, n//2 + 1):
        for p in cycle_partitions(n-i, i):
            yield [i] + p


def solution(w, h, s):
    grid = 0
    for cpw in cycle_partitions(w):
        for cph in cycle_partitions(h):
            m = cycle_count(cpw, w)*cycle_count(cph, h)
            grid += m*(s**sum([sum([gcd(i, j) for i in cpw]) for j in cph]))

    return str(grid//(factorial(w)*factorial(h)))
