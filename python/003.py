#!/usr/bin/env python3

N = 600851475143


def factorize(f, number):
    """
    First find factors of number. Ignore the smaller, move to larger
    """
    if f == 1:
        return number
    for i in range(3, number + 1, 2):
        if number % i == 0:
            return factorize(i, number // i)
    return f


def main():
    answer = factorize(3, N)
    print(answer)


if __name__ == '__main__':
    main()
