def fizz(i):
    if i % 3 == 0:
        return 'Fizz'

def buzz(i):
    if i % 5 == 0:
        return 'Buzz'

def fizzbuzz(i):
    if fizz(i) and buzz(i):
        return 'FizzBuzz'

for i in range(1, 101):
    print(fizzbuzz(i) or fizz(i) or buzz(i) or i)

