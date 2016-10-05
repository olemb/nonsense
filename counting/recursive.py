def f(n=10):
    if n > 1:
        f(n - 1)
    print(n)

f()
