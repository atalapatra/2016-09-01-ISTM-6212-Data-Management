#!/usr/bin/env python

"""
A filter that removes 15 stop words from the input.
"""

import fileinput
import string

stops = ['and','about','out','be','did','this','there','some','she','to','can','with','if','you','the']

def process(line):
    """For each line of input, removes the stop words."""
    
    line = line[:-1]
    while line not in stops:
          print(line)
          break

for line in fileinput.input():
    process(line)
