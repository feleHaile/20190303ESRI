#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("f0: {}".format(f0), '\n')


def lower_case(f):
    return f.lower()

f1 = sorted(fruits, key=str.lower)
print("f1: {}", format(f1), '\n')

f2 = sorted(fruits, key=len)
print("f2: {}", format(f2), '\n')

def mycustom(fruit):
    return len(fruit), fruit.lower()

f2 = sorted(fruits, key=mycustom)
print("f2: {}", format(f2), '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]
def by_last_name(person):
    return person[1], person[0]

for first_name, last_name, _ in sorted(people, key=by_last_name):
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, _ in sorted(people, key=lambda p: (p[1]):
    print(first_name, last_name)
print('-' * 60)
