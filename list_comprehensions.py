#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.title())
print("f0:", f0, '\n')

f1 = [f.title() for f in fruits]
print("f1:", f1, '\n')


suits = 'C D H S'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards = [(r, s) for s in suits for r in ranks]
print(cards, '\n')

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


names = [f'{fn} {ln}' for fn, ln, _ in people if fn.startswith('L')]

print(names, '\n')

# [(EXPR1, EXPR1) for VAR ... in ITERABLE ... if CONDITION ...]

last_names = [p[1] for p in people]
print(last_names, '\n')

last_names_gen = (p[1] for p in people)

print(last_names_gen)

print("first loop:")
for last_name in last_names_gen:
    print(last_name)
print()

print("second loop:")
for last_name in last_names_gen:
    print(last_name)
print()

del last_names_gen


f1_gen = (f.title() for f in fruits)
f1_items = list(f1_gen)
print(f1_items)
