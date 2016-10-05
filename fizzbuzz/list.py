q = [''] * 101

for i in range(3, 101, 3):
    q[i] = 'fizz'

for i in range(5, 101, 5):
    q[i] += 'buzz'

for i in range(1, 101):
    print(q[i].capitalize() or i)

