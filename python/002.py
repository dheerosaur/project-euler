#!/usr/bin/env python3

# There are some interesting mathematical proofs and approaches on
# this page: https://projecteuler.net/thread=2;page=5

N = 4e9  # 4 million


def main3():
    """
    Every 3d cycle. Fewer iterations

       first   second   =>   next
       ===========================
       odd     even     =>   odd
       even    odd      =>   odd
       odd     odd      =>   even

    and so on ...

       first   second   =>   next
       ===========================
       x        y       =>   x+y
       y        x+y     =>   x+2y
       x+y      x+2y    =>   2x+3y

    Comparing the tables here, you can see that (odd, even)
    repeats on every third cycle as a series of (x+2y, 2x+3y)
    """
    total, x, y = 0, 1, 2  # x is odd, y is even
    while y <= N:
        total += y
        x, y = x + 2 * y, 2 * x + 3 * y
    print(total)


def main2():
    "Do two numbers in the loop at once. Half as many loops"
    total, first, second = 0, 1, 2
    while second <= N:
        if first % 2 == 0:
            total += first
        if second % 2 == 0:
            total += second
        first, second = first + second, first + 2 * second
    print(total)


def main():
    "Brute force"
    total, first, nxt = 0, 1, 2
    while first <= N:
        if first % 2 == 0:
            total += first
        first, nxt = nxt, first + nxt
    print(total)


if __name__ == '__main__':
    main3()
