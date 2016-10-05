for i in range(1, 101):
    print([i, 'Fizz', 'Buzz', 'Fizzbuzz'][(not i % 3) | (not i % 5) << 1])
