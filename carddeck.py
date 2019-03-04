#!/usr/bin/env python
import random

class CardDeck():
    SUITS = 'C D H S'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


    def __init__(self, dealer):
        self._dealer = dealer
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = f'{rank}-{suit}'
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):
        return self._dealer

    # dealer = property(dealer)
    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @property
    def spam(self):
        return

    @property
    def ham(self):
        return

    @ham.setter
    def ham(self, value):
        pass

    def shuffle(self):
        random.shuffle(self._cards)
