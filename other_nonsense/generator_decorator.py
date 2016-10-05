from __future__ import print_function

def pointless(func):
    def f():
        (args, kwargs) = yield
        while True:
            (args, kwargs) = yield func(*args, **kwargs)

    gen = f()
    next(gen)

    return lambda *args, **kwargs: gen.send((args, kwargs))

@pointless
def double(x):
    return x * 2

print(double(2))
print(double(3))
