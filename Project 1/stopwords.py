#!/usr/bin/env python

"""
A filter that removes at least ten common words of English text, commonly known as “stop words”.
"""

import fileinput

def process(line):
    """For each line of input, remove common words of English text, commonly known as “stopwords”."""
    stopwords = ["the","of","and","to","a","in","that","is","was","for","it","with","as","on","be","at","by","i"]
    for word in line.split():
        if word not in stopwords:
            print(word)

for line in fileinput.input():
    process(line)
