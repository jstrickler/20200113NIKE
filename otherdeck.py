#!/usr/bin/env python
from cardbase import CardBase


class OtherDeck(CardBase):
    def draw(self):
        print("drawing....")


o = OtherDeck()

