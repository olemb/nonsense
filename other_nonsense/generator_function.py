"""
Pointless misuse of generator to implement function.
"""
def f():
    n = yield
    while True:
        n = yield n * n

gen = f()
next(gen)
square = gen.send

# Prints 4.
print(square(2))
