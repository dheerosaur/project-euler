#!/usr/bin/env python3


def main(data):
    numbers = [int(n) for n in data.strip().split('\n')]
    print(str(sum(numbers))[:10])


if __name__ == '__main__':
    with open('data/013') as f:
        main(f.read())
