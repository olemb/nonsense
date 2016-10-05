import sys

class _():
    def __getattr__(self, char):
        sys.stdout.write(char)
        return self

    @property
    def _(self):
        sys.stdout.write(' ')
        return self

    @property
    def __(self):
        sys.stdout.write(',')
        return self

    @property
    def ___(self):
        sys.stdout.write('!')
        return self

    @property
    def ____(self):
        sys.stdout.write('\n')
        return self

_ = _()

_.H.e.l.l.o.__._.w.o.r.l.d.___.____
