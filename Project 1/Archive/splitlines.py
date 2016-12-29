#!/usr/bin/env python

"""
A filter that splits lines of text into one word per line.
"""

import fileinput
import re

def process(line):
    """For each line of input, split lines of text into one word per line."""
    for word in re.findall(r'\w+', line):
        print(word)

for line in fileinput.input():
    process(line)
