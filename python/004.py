#!/usr/bin/env python3

U = 999  # upper limit
L = 900  # lower limit


def is_palindrome(n):
    """
    Finds if a number is a palindrome by converting it to a string
    and then comparing it to its reverse
    """
    string = str(n)
    return string == string[::-1]


def has_three_digit_factors(n):
    """
    Iterate down from 999 and see if the number
    """


def main3():
    """
    Construct palindromes out of 3 digit numbers and then check if they
    have 3-digit factors
    """
    for i in range(U, L, -1):
        palindrome = int(str(i) + str(i)[::-1])
        for j in range(U, L, -1):
            if palindrome % j == 0 and (palindrome // j) < (U + 1):
                print(palindrome)
                return


def main2():
    "One-liner brute-force solution"
    print(max([(x * y) for x in range(L, U + 1) for y in range(L, U + 1)
               if str(x * y) == str(x * y)[::-1]]))


def main():
    answer = 0
    for i in range(U, L, -1):
        for j in range(i, L, -1):
            product = i * j
            if is_palindrome(product) and product > answer:
                answer = product
    print(answer)


if __name__ == '__main__':
    main()
