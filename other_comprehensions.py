#!/usr/bin/env python
"""
Demo for Esri workshop
"""
from pprint import pprint

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

def main():
    comp_demo()

def comp_demo():
    """
    Display how to make dict and set comprehensions

    :return: None
    """
    fdict = { f.lower():f for f in fruits}
    pprint(fdict)

    food = ['spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'EGGS',
            'SPAM', 'Spam', 'SPAM', 'Eggs', 'Spam']

    values = {f.lower() for f in food} # unique by case
    print(values)

def doit(file_name):
    """
    Some more fancy words here.

    :param file_name: Name of file to open -- must be in .txt format
    :return: Length of new file
    """

if __name__ == '__main__':
    main()
