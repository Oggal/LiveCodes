#!/usr/bin/env python3

import cmd

from demos.fizzbuzz import fizzbuzz
from demos.primes import PrimeFinder
from demos.recursion import NoisyFib

IsPrime = PrimeFinder.checkPrime

class WombatConsole(cmd.Cmd):
    '''Wombat Console'''

    prompt = '-> :'

    def do_fizzbuzz(self, line):
        """Prints fizzbuzz up to top"""
        try:
            fizzbuzz(int(line))
        except ValueError:
            print("Please enter a number...")

    def do_primeCheck(self, line):
        """checks if a number is prime"""
        try:
            res = IsPrime(int(line))
            if res:
                print("{} is prime".format(line))
            else:
                print("{} is not prime".format(line))
        except ValueError:
            print("Please enter a number...")

    def do_fibinoisy(self, line):
        """Prints fibonacci up to N"""
        try:
            res = NoisyFib.NoisyFib(int(line))
            print()
            print("Result: {}".format(res))
        except ValueError:
            print("Please enter a number...")

    def do_exit(self, line):
        return True
    
    def do_EOF(self, line):
        return True

if __name__ == "__main__":
    WombatConsole().cmdloop()