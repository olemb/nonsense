#!/usr/bin/env python3
import re

TEXT = """You may wonder what this paragraph is for. It is simply a way for
me to generate some pointless data as input. The meaning of these
words do not affect the outcome of executing the program on your
electronic computing device."""

words = re.findall('\w+', TEXT)
for i in sorted(set(map(len, words))):
    print(i)
