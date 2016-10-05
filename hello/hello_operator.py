from __future__ import print_function

class _(object):
    def __init__(self):
        self.__ = 0
    
    def __pos__(self):
        self.__ = (self.__ << 1) | 1
        return self

    def __neg__(self):
        self.__ <<= 1
        return self

    def __invert__(self):
        while self.__:
            print(chr(self.__ & 0xff), sep='', end='')
            self.__ >>= 8
        return self
_ = _()

[~
   ---+--+- +-+--++- --++-++- --++-++- ++++-++- --++-+-- -----+--
   +++-+++- ++++-++- -+--+++- --++-++- --+--++- +----+-- -+-+----
_]
