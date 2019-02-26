#!/usr/bin/env python3

N = 10001


def is_prime(n):
    "Brute force way to test for a prime number"
    upto = int(n ** .5) + 1  # ceiling
    for i in range(3, upto, 2):
        if n % i == 0:
            return False
    return True


def main():
    """
    Just iterate over odd numbers and check for prime numbers
    """
    n, last_prime, count = 3, 3, 2
    while True:
        n += 2
        if is_prime(n):
            count += 1
            last_prime = n
        if count == N:
            break
    print(last_prime)


if __name__ == '__main__':
    main()
