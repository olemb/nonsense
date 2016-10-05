from __future__ import print_function

class _(object):
    def __init__(self):
        self.n = 0
        self.num_bits = 0
        
    def _push(self, bit):
        self.n = (self.n << 1) | bit
        self.num_bits += 1
        if self.num_bits == 8:
            print(chr(self.n), sep='', end='')
            self.n = self.num_bits = 0

    def __pos__(self):
        self._push(1)
        return self

    def __neg__(self):
        self._push(0)
        return self

_ = _()
