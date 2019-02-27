#!/usr/bin/env python3
N = 500


def num_divisors(n):
    lower, upper = 1, n
    answer = 0
    while lower < upper:
        if n % lower == 0:
            upper = n // lower
            answer += 1 if upper == lower else 2
        lower = lower + 1
    return answer


def main():
    n = 1
    while True:
        tr_number = int(n * (n + 1) / 2)
        if num_divisors(tr_number) > N:
            break
        n += 1
    print(tr_number)


if __name__ == '__main__':
    main()
