#!/usr/bin/env python3
from math import pi

PI_DIGITS = '{:.100}'.format(pi).split('.')[1]

for char in 'AFIBDGMKEg':
    print(int(PI_DIGITS[ord(char) - ord('A')]) or 10)
