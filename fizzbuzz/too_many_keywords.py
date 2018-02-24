for i in range(1, 101):
    print(''.join(word if i % n == 0 else '' for (word, n) in [('Fizz', 3), ('Buzz', 5)]) or i)
