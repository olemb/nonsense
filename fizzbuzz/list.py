q = [''] * 101

for i in range(3, 101, 3):
    q[i] = 'Fizz'

for i in range(5, 101, 5):
    q[i] += 'Buzz'

for i in range(1, 101):
    print(q[i] or i)
