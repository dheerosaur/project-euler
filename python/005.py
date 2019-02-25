#!/usr/bin/env python3
N = 20


def main():
    "Brute force"
    product = 1
    for i in range(2, N + 1):
        if product % i == 0:
            continue
        for j in range(2, N + 1):
            if (product * j) % i == 0:
                product = product * j
                break
    print(product)


if __name__ == '__main__':
    main()
