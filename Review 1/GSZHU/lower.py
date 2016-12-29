#!/usr/bin/env python

"""
A filter that lowercase the input.
"""

import fileinput


def process(line):
    """For each line of input, lowercase it."""
    line = line.strip()
    print(line.lower())


for line in fileinput.input():
    process(line)
