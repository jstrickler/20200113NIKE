#!/usr/bin/env python
from dataclasses import dataclass
import random

from cardbase import CardBase

class OutOfCardsError(Exception):
    pass

@dataclass
class Card:
    rank: str
    suit: str

class CardDeck(CardBase):
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()


    def __init__(self, dealer_name):
        self.dealer = dealer_name
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):
        return self._dealer_name

    @dealer.setter
    def dealer(self, value):
        if isinstance(value, str):
            self._dealer_name = value
        else:
            bad_type_name = type(value).__name__
            raise TypeError(f"Dealer name must be a string, not a(n) {bad_type_name}")

    # reproduce object
    def __repr__(self):
        my_name = type(self).__name__
        return f"{my_name}('{self.dealer}')"

    #  eval(repr(X)) == X

    # display object for humans
    # def __str__(self):
    #     return f"CardDeck, with {self.dealer} dealing"

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if len(self) == 0:
            raise OutOfCardsError("Sorry! No Cards for you!")
        return self._cards.pop()

    def __len__(self):   # called by len(instance)
        return len(self._cards)


    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    @staticmethod
    def hello():
        print("Hi Mom!")

    def __add__(self, other):
        tmp = type(self)(self.dealer)
        tmp._cards = self._cards + other._cards
        return tmp

    def __sub__(self, other):
        print("HI MOM!!")
