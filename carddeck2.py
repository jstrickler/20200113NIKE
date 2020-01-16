#!/usr/bin/env python
from dataclasses import dataclass, field
from typing import List, ClassVar
import random
from datetime import Date
from pprint import pprint
"""
Provide cards and card deck
"""

@dataclass
class Card:
    """
    One standard playing card
    """
    rank: str
    suit: str

    def __repr__(self):
        return f"{self.rank}-{self.suit}"

@dataclass
class CardDeck:
    """
    A deck of standard playing cards

    Contains a list of Card objects
    """
    SUITS: ClassVar = "Clubs Diamonds Hearts Spades".split()
    RANKS: ClassVar = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    cards: List[Card] = field(init=False, default_factory=list, repr=False)

    dealer: str
    _dealer: str = field(init=False, repr=False)

    def __post_init__(self):
        for suit in CardDeck.SUITS:
            for rank in CardDeck.RANKS:
                card = Card(rank, suit)
                self.cards.append(card)

    @property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, value):
        if isinstance(value, str):
            self._dealer = value
        else:
            raise ValueError(f"Dealer must be string, not {type(value).__name__}")

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

if __name__ == '__main__':
    d1 = CardDeck("Bob")
    print(d1)
    try:
        x = CardDeck(123)
    except ValueError as err:
        print(err)

    d1.shuffle()

    print("Cards:", end=' ')
    pprint(d1.cards)
    print()

    print("Drawing:")
    for _ in range(10):
        print(d1.draw())
    print()

    print(d1.dealer)

    d2 = CardDeck("Wanda")
    print(len(d1), len(d2))


@dataclass(frozen=True)
class President:
    "One POTUS"
    first_name: str
    last_name: str
    dob: Date
    dod: Date
    party: str

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    @staticmethod
    def _mkdate(raw_date):
        if raw_date != "NONE":
            raw_year, raw_month, raw_day = raw_date.split('-')
            d = Date(int(raw_year), int(raw_month), int(raw_day))
        else:
            d = None

        return d

    def __post_init__(self):
        # Note: replace the following code to use the DB API to get
        # data from the presidents.db database.
        # You will probably need to access it as "DATA/presidents.db"
        # You will no longer need the _mkdate() method
        with open("DATA/presidents.txt") as pfile:
            for line in pfile:
                flds = line.split(":")
                if int(flds[0]) == int(index):
                    self.last_name = flds[1]

                    self.first_name = flds[2]

                    self._bdate = self._mkdate(flds[3])
                    self._ddate = self._mkdate(flds[4])

                    self._bplace = flds[5]
                    self._bstate = flds[6]

                    self._ts_date = self._mkdate(flds[7])
                    self._te_date = self._mkdate(flds[8])

                    self._party = flds[9]

                    break
            else:
                raise ValueError("Invalid term number")
