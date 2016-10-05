numbers = list(range(1, 101))
fizz = set(numbers[3-1::3])
buzz = set(numbers[5-1::5])

for i in numbers:
    if i in fizz and i in buzz:
        print('Fizzbuzz')
    elif i in fizz:
        print('Fizz')
    elif i in buzz:
        print('Buzz')
    else:
        print(i)

