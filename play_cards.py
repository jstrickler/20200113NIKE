#!/usr/bin/env python
"""
Play some cards
"""
from carddeck import CardDeck, OutOfCardsError
from jokerdeck import JokerDeck

D1 = CardDeck("Bob")
D2 = CardDeck("Anna")
try:
    D3 = CardDeck(123)
except TypeError as err:
    print(err)

print(D1, D2)

D1.shuffle()
print(D1.cards)
for _ in range(7):
    print(D1.draw())



print(D1.get_ranks())
print(CardDeck.get_ranks())

while True:
    try:
        CARD = D1.draw()
    except OutOfCardsError as err:
        print(err)
        break

print(len(D1), len(D2))

J1 = JokerDeck("Albert")
J1.shuffle()
print(len(J1))
print(J1)
print(J1.cards)
print(JokerDeck.mro())
J1.yell()

RESULT = D1 + D2 + J1

print(RESULT)
print(len(RESULT))

DIFF = D1 - D2
