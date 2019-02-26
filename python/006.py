#!/usr/bin/env python3
N = 100


def main():
    """
    Sum of squares of numbers upto N - brute
    Sum of numbers squared = n.n+1/2 ** 2
    """
    sum_of_squares = sum(n * n for n in range(N + 1))
    square_of_sum = sum(range(N+1)) ** 2
    print(square_of_sum - sum_of_squares)


if __name__ == '__main__':
    main()
