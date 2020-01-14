#!/usr/bin/env python

colors = [('blue', 5), ('purple', 6), ('orange', 4), ('brown', 2)]

for color in colors:
    print(color)
print()

ci =  iter(colors)
print(ci)

print(next(ci))
print(next(ci))

for color in ci:
    print(color)

print('-' * 60)

ci = iter(colors)
while True:
    try:
        color, number = next(ci)
    except StopIteration:
        break
    print(color, number)

