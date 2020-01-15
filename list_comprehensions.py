#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

# [EXPR for VAR ... in ITERABLE if COND ...]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

food = ['spam', 'spam', 'spam', 'spam', 'spam',
        'lobster thermidor', 'spam',
        'spam', 'spam', 'spam', 'spam', 'eggs', 'ham',
        'spam', 'spam', 'truffles', 'spam']

good_foods = [f for f in food if f != 'spam']
print(good_foods)

lod = [
    {'a': 1, 'b': 2, 'c': 3},
    {'a': 3, 'b': 5, 'c': 8},
]

c_fields = [(d['a'], d['c']) for d in lod]
print(c_fields)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')

# list comprehensions
# dict comprehensions
# set comprehensions
# generator expressions

food = ['spam', 'spam', 'spam', 'spam', 'spam',
        'lobster thermidor', 'spam',
        'spam', 'spam', 'spam', 'spam', 'eggs', 'ham',
        'spam', 'spam', 'truffles', 'spam']

unique_foods = {f for f in food if f != 'spam'}
print(unique_foods)
print(type(unique_foods))

ff = {f:len(f) > 6 for f in fruits if f.startswith('p')}
print(ff)

