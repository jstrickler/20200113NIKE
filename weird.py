#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


fg = (f.upper() for f in fruits)

print(fg)

for fruit in fg:
    print(fruit)
print('-' * 60)

fg = (f.upper() for f in fruits)
print(next(fg))
print(next(fg))
print()
for fruit in fg:
    print(fruit)
print()
# print(next(fg))

fg = (f.upper() for f in fruits)
grab3 = (x[:3] for x in fg)

print(list(grab3))

# def foo():
#     foo()
#
# foo()

