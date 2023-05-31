#!/usr/bin/env python3

class PrimeFinder:

    @staticmethod
    def checkPrime(n: int) -> bool:
        '''Checks if a number is prime'''
        if n == 1:
            return False
        if n > 2:
            half_n = n // 2
        for i in range(2, half_n):
            if n % i == 0:
                return False
        return True
