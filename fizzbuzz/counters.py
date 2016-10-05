fizz = 3
buzz = 5

for i in range(1, 101):
    if fizz == buzz == 1:
        print('Fizzbuzz')
    elif fizz == 1:
        print('Fizz')
    elif buzz == 1:
        print('Buzz')
    else:
        print(i)

    fizz = (fizz - 1) % 3
    buzz = (buzz - 1) % 5
