#!/usr/bin/env python3

N = 1000


def main4():
    """
    Use mathematical approach to compute this in linear time
    - sum of all x multiples until n is x.(n/x).(n/x+1)/2
    - add sum of x and y and subtract sum of x.y because it's added twice

    This is an O(1) function
    """

    def xsn(x, n):
        "x multiples - sum until - n"
        return x * (n // x) * (n // x + 1) // 2

    # (N - 1) because the problem asks for "below N"
    answer = xsn(3, N - 1) + xsn(5, N - 1) - xsn(15, N - 1)
    print(answer)


def main3():
    """
    Using sets (from forums)
    Surprisingly, this was the fastest even until 1e9
    """
    numbers = set(range(0, N, 3)) | set(range(0, N, 5))
    print(sum(numbers))


def main2():
    "Brute force method"
    answer = 0
    for i in range(1, N):
        if i % 3 == 0 or i % 5 == 0:
            answer = answer + i
    print(answer)


def main():
    "Not better than brute force, but shorter"
    numbers = (x for x in range(1, N) if x % 3 == 0 or x % 5 == 0)
    print(sum(numbers))


if __name__ == '__main__':
    main()
