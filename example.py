#!/usr/bin/env python3

import cmd

from demos.fizzbuzz import fizzbuzz


class WombatConsole(cmd.Cmd):
    '''Wombat Console'''

    prompt = '-> :'

    def do_fizzbuzz(self, line):
        """Prints fizzbuzz up to top"""
        try:
            fizzbuzz(int(line))
        except ValueError:
            print("Please enter a number...")

    def do_exit(self, line):
        return True
    
    def do_EOF(self, line):
        return True

if __name__ == "__main__":
    WombatConsole().cmdloop()