#!/usr/bin/env python
from pprint import pprint

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'IAD': 'Dulles',
}

print(airports, '\n')
print(airports['RDU'], '\n')
print(airports.get('PDX'), '\n')
print(airports.get('PDX', 100), '\n')

more_airports = {
    'PDX': 'Portland',
    'ALB': 'Albany',
    'IAD': 'Washington Dulles',
}

airports.update(more_airports)
pprint(airports)

d = {'a': 5, 'b': 8, 'm': 99, 'e': 12}

for thing in d:
    print(thing)
print()


for k, v in d.items():
    print(k, v)
print()


for k, v in sorted(d.items()):
    print(k, v)

for k, v in sorted(d.items(), key=lambda e: (e[1], e[0])):
    print(k, v)

