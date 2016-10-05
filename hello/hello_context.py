import sys

class _(object):
    _ = {'n': 0, 'level': 0}

    def __init__(self, value):
        self.value = value

    def __enter__(self):
        self._['n'] <<= 1
        self._['n'] |= self.value
        self._['level'] += 1
        return self

    def __exit__(self, *_):
        self._['level'] -= 1
        if self._['level'] == 0:
            sys.stdout.write(chr(self._['n'] & 0xff))

        return False

_, __ = _(0), _(1)
# from hello.context import _

with _:
    with __:
        with _:
            with _:
                with __:
                    with _:
                        with _:
                            with _:
                                pass
with _:
    with __:
        with __:
            with _:
                with _:
                    with __:
                        with _:
                            with __:
                                pass
with _:
    with __:
        with __:
            with _:
                with __:
                    with __:
                        with _:
                            with _:
                                pass
with _:
    with __:
        with __:
            with _:
                with __:
                    with __:
                        with _:
                            with _:
                                pass
with _:
    with __:
        with __:
            with _:
                with __:
                    with __:
                        with __:
                            with __:
                                pass
with _:
    with _:
        with __:
            with _:
                with __:
                    with __:
                        with _:
                            with _:
                                pass
with _:
    with _:
        with __:
            with _:
                with _:
                    with _:
                        with _:
                            with _:
                                pass
with _:
    with __:
        with __:
            with __:
                with _:
                    with __:
                        with __:
                            with __:
                                pass
with _:
    with __:
        with __:
            with _:
                with __:
                    with __:
                        with __:
                            with __:
                                pass
with _:
    with __:
        with __:
            with __:
                with _:
                    with _:
                        with __:
                            with _:
                                pass
with _:
    with __:
        with __:
            with _:
                with __:
                    with __:
                        with _:
                            with _:
                                pass
with _:
    with __:
        with __:
            with _:
                with _:
                    with __:
                        with _:
                            with _:
                                pass
with _:
    with _:
        with __:
            with _:
                with _:
                    with _:
                        with _:
                            with __:
                                pass
with _:
    with _:
        with _:
            with _:
                with __:
                    with _:
                        with __:
                            with _:
                                pass
