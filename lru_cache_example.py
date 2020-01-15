#!/usr/bin/env python
from functools import lru_cache


@lru_cache(None)
def addem(a, b):
    print("adding")
    return a + b


data = [
    (5, 3),
    (5, 3),
    (5, 3),
    (5, 3),
    (10, 2),
    (10, 2),
    (5, 3),
    (10, 2),
]

for i, j in data:
    print(addem(i, j))
