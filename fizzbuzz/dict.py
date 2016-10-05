buzzed = {
    (True, False): 'Fizz',
    (False, True): 'Buzz',
    (True, True): 'Fizzbuzz',
}

for i in range(1, 101):
    print(buzzed.get((not i % 3, not i % 5), i))
