for i in range(1, 101):
    print([i, 'Fizz', 'Buzz', 'FizzBuzz'][(not i % 3) | (not i % 5) << 1])
