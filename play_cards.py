#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Fred")  # create an instance of CardDeck
print(d1)
# print(dir(d1))
# x = getattr(d1, '_dealer')
# print(x)

print(d1.dealer)

d1.dealer = 'Mary'
print(d1.dealer)

d1.shuffle()
print(d1.cards)

# d1.shuffle()
# CardDeck.shuffle(d1)
# print(d1.draw())
print('-' * 60)
j1 = JokerDeck('Betty')
j1.shuffle()
print(j1.cards)
