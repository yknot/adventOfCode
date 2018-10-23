from math import sqrt
from itertools import count, islice


def isPrime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


h = 0

b = 81
b *= 100
b -= -100000
c = b
c -= -17000

while True:
    f = 1
    d = 2

    # while True:
    #     e = 2
    #     while True:
    #         # g = d
    #         # g *= e
    #         # g -= b
    #         if d * e - b == 0:
    #             print(d, e, b)
    #             print('set to 0')
    #             f = 0
    #         # e -= -1
    #         # g = e
    #         # g -= b
    #         e += 1
    #         if e - b == 0:
    #             print('g == 0')
    #             print()
    #             break

    # inner loop replacement
    f = 1 if isPrime(b) else 0
    e = b
    g = b

    # d -= -1
    # g = d
    # g -= b
    # if not g:
    #     break
    # outer loop replacement
    d = b
    g = b

    if not f:
        h -= -1
    g = b
    g -= c
    if not g:
        break
    b -= -17

print(h)
