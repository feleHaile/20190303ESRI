#!/usr/bin/env python

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip()

mary_in = trimmed('DATA/mary.txt')
for line in mary_in:
    print(line)

def wacky():
    yield "Python"
    yield "is"
    yield "wacky"
    yield "and wonderful"

gen = wacky()
for word in gen:
    print(word, end=' ')
print()
print("---")
for word in gen:
    print(word, end=' ')
print()
