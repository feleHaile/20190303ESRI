#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft', "Gates Foundation"

values = 1,

print(person[0], person[2], person[-1])
print(type(person), len(person))

# first_name, last_name, product = person

first_name, last_name, product = person[:3]

first_name, last_name, *product = person

print(first_name, last_name, product)

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)


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

print()
for first_name, last_name, *_ in people:
# for person in people:
    # print(person[:2])
    print(first_name, last_name, product)
print()

for i, value in enumerate(values):
    print(i, value)
print()

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

for abbr, name in airports.items():
    print(abbr, name)
print()


p2 = [p[:2] for p in people]
