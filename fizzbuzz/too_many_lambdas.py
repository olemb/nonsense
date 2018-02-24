_ = list(map(print, map(lambda n: ((lambda n: 'Fizz' if n % 3 == 0 else '')(n) + (lambda n: 'Bizz' if n % 5 == 0 else '')(n)) or n, map(lambda n: n + 1, range(100)))))
