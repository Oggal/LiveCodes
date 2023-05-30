#!/usr/bin/env python3


def fizzbuzz(top: int = 100):
    """Prints fizzbuzz up to top"""
    for i in range(1, top + 1):
        a = False
        if i % 3 == 0:
            a = True
            print("fizz", end="")
        if i % 5 == 0:
            a = True
            print("buzz", end="")
        if not a:
            print(i, end="")
        print()