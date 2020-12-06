def get_digits(n):
    return list(map(int, f'{n:.100}'.split('.')[1]))

for digit in get_digits(1 / 8.10000007)[:10]:
    print(digit or 10)
