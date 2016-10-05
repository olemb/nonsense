for i in range(1, 101):
    fizz = bool(i % 3 == 0)
    buzz = bool(i % 5 == 0)
    if fizz and buzz:
        print('Fizzbuzz')
    elif fizz:
        print('Fizz')
    elif buzz:
        print('Buzz')
    else:
        print(i)
