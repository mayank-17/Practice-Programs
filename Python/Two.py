def fib_to(n):
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

from numpy import array

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

test = int(input())
for i in range(test):
    n = int(input())
    P = get_primes(n)
    FIB = fib_to(n)
    m = len(FIB)
    P = array(P)
    FIB = array(FIB)
    P = P[P < m]
    print(sum(list(FIB[P])))
