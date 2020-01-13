#!/usr/bin/env python

import timeit

setup_code = """b = 'banana'"""

codes = [
    '''b[0] == "b"''',
    '''b.startswith('b')''',
]

for code in codes:
    t = timeit.Timer(code, setup_code)
    print(code, '\n')
    print(t.timeit(1000000))
    print()

