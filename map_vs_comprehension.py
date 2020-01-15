#!/usr/bin/env python

import timeit


setup_code = """
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]
"""

codes = [
    '''f0 = (f.upper() for f in fruits)''',
    '''f0 = map(str.upper, fruits)''',
    '''f0 = [f.upper() for f in fruits]''',
    '''f0 = list(map(str.upper, fruits))''',
]

for code in codes:
    t = timeit.Timer(code, setup_code)
    print(code, '\n')
    print(t.timeit(10000))
    print()

