class BaseBuzz:
    pass


class NoBuzz(BaseBuzz):
    def __str__(self):
        return ''

    def __add__(self, other):
        return other


class ValueBuzz(BaseBuzz):
    pass


class Fizz(ValueBuzz):
    interval = 3

    @classmethod
    def is_fizz(self, n):
        return n % Fizz.interval == 0

    def __str__(self):
        return 'Fizz'

    def __add__(self, other):
        if isinstance(other, Buzz):
            return FizzBuzz()
        else:
            raise ValueError('invalid buzz operation')


class Buzz(ValueBuzz):
    interval = 5

    @classmethod
    def is_buzz(self, n):
        return n % Buzz.interval == 0

    def __str__(self):
        return 'Buzz'


class FizzBuzz(Fizz, Buzz):
    interval = 5

    def __str__(self):
        return Fizz.__str__(self) + Buzz.__str__(self)


for i in range(1, 101):

    buzzword = NoBuzz()

    if Fizz.is_fizz(i):
        buzzword += Fizz()

    if Buzz.is_buzz(i):
        buzzword += Buzz()

    if isinstance(buzzword, NoBuzz):
        print(i)
    else:
        print(buzzword)
