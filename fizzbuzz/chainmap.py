"""Required Python 3.3."""
from collections import ChainMap

class Numberer(object):
    def __getitem__(self, i):
        return i

class FizzerBuzzer(object):
    def __init__(self, n, word):
        self.n = n
        self.word = word

    def __getitem__(self, i):
        if not i % self.n:
            return self.word
        else:
            raise KeyError

chainmap = ChainMap(FizzerBuzzer(15, 'FizzBuzz'),
                    FizzerBuzzer(3, 'Fizz'),
                    FizzerBuzzer(5, 'Buzz'),
                    Numberer())
for i in range(1, 101):
    print(chainmap[i])

