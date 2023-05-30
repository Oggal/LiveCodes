#!/usr/bin/env python3
class NoisyFib:
    __tab = 0
    @classmethod
    def NoisyFib(cls, n: int):
        
        print("{}Calling NoisyFib({})".format(("\t" * cls.__tab) ,n))
        cls.__tab += 1
        if n < 2:
            print("{}Returning 1".format(("\t" * cls.__tab)))
            cls.__tab -= 1
            return 1
        else:
            a = cls.NoisyFib(n - 1)
            b = cls.NoisyFib(n - 2)
            print("{}Returning {} + {}".format(("\t" * cls.__tab), a, b))
            cls.__tab -= 1
            return a + b