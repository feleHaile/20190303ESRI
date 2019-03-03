#!/usr/bin/env python
from collections import namedtuple

person = 'Bill', 'Gates', 'Microsoft'
print(person[0])

Person = namedtuple('Person', 'first_name last_name product')

person = Person('Bill', 'Gates', 'Microsoft')
print(person.first_name)
print(type(person))
