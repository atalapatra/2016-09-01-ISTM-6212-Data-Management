#!/usr/bin/env python

"""
A filter that make the input one word a line.
"""

import fileinput
import re 

def process(line):
    """For each line of input, print one word each line."""
    line = line.strip()
    temp = re.compile('\w+')
    line = temp.findall(line)
    for words in line:
    	if len(words) >=2:
            print(words)


for line in fileinput.input():
    process(line)
