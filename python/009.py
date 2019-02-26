#!/usr/bin/env python3

N = 1000


def main():
    for a in range(1, N):
        for b in range(a, N):
            product = a * a + b * b
            c = int(product ** 0.5)
            if (product == c * c) and (a + b + c) == 1000:
                print(a * b * int(c))
                break


if __name__ == '__main__':
    main()
