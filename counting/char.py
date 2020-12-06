import string
for i in range(256):
    char = chr(i)
    if char in string.digits:
        print(int(char) + 1)
