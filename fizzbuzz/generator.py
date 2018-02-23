def gen():
    while True:
        for char in '001021001201003':
            yield ['', 'Fizz', 'Buzz', 'FizzBuzz'][int(char)]

for word, i in zip(gen(), range(1, 101)):
    print(word or i)
