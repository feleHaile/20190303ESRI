#!/usr/bin/env python
from pprint import pprint

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

fdict = { f.lower():f for f in fruits}
pprint(fdict)

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'EGGS',
        'SPAM', 'Spam', 'SPAM', 'Eggs', 'Spam']

values = {f.lower() for f in food}
print(values)
