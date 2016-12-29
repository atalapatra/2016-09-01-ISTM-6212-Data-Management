#!/usr/bin/env python

"""
A filter that transforms text into lower case.
"""

import fileinput

def process(line):
    """For each line of input, transform text into lower case."""
    print(line.strip().lower())

for line in fileinput.input():
    process(line)
