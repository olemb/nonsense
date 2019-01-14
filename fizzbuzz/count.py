fizz = 0
buzz = 0

for i in range(1, 101):
    text = ''

    fizz += 1
    buzz += 1

    if fizz == 3:
        text += 'Fizz'
        fizz = 0

    if buzz == 5:
        text += 'Buzz'
        buzz = 0

    print(text or i)
