for i in range(1, 101):
    fizz = not i % 3
    buzz = not i % 5
    if fizz and buzz:
        print('FizzBuzz')
    elif fizz:
        print('Fizz')
    elif buzz:
        print('Buzz')
    else:
        print(i)
