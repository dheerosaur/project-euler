#!/usr/bin/env python3
from itertools import chain
N = 2000000


def main_seive():
    """
    - Using seive of eratosthanes starting from the squares
        Runs in about 2.56 seconds
    - Further optimization by starting with all evens removed
    """
    primes = [0, 1] * (N // 2)
    upto = (N ** 0.5 + 1)

    i = 3
    while i < upto:
        if primes[i]:
            k = 0
            j = i ** 2 + k * i
            while j < N:
                primes[j] = 0
                k += 1
                j = i ** 2 + k * i
        i += 2

    print(2 + sum([p for p in range(N) if primes[p]]))


def main():
    """
    Brute force method with minor optimizations like stopping at
    square root, iterating only over odd numbers etc.
    """

    n = 3  # start with 3
    primes = [2, 3]

    def is_prime(n):
        "Brute force way to test for a prime number"
        upto = int(n ** .5) + 1  # ceiling

        # First check all primes below that number
        for i in chain(primes, range(primes[-1], upto, 2)):
            if n % i == 0:
                return False
            if i > upto:
                break

        return True

    while n < N:
        n += 2
        if is_prime(n):
            primes.append(n)

    print(sum(primes))


if __name__ == '__main__':
    main_seive()
