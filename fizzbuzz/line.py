for i in range(1, 101):
    line = ''
    if not i % 3:
        line += 'fizz'
    if not i % 5:
        line += 'buzz'
    print(line.capitalize() or i)

