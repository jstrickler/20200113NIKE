#!/usr/bin/env python
from carddeck import CardDeck, Card

class Thing():
    def yell(self):
        print("AIIIEEEEEEEEEEEEE")

class JokerDeck(CardDeck, Thing):

    def _make_deck(self):
        super()._make_deck()
        j1 = Card(1, 'Joker')
        j2 = Card(2, 'Joker')
        self._cards.append(j1)
        self._cards.append(j2)


