fizz = set(range(3, 101, 3))
buzz = set(range(5, 101, 5))
fizzbuzz = fizz & buzz

for i in range(1, 101):
    if i in fizzbuzz:
        print('Fizzbuzz')
    elif i in fizz:
        print('Fizz')
    elif i in buzz:
        print('Buzz')
    else:
        print(i)

