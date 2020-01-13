#!/usr/bin/env python
from copy import deepcopy

x = 5    #  x = int(5)
#  value  type  ID
print(x, type(x), id(x))

y = x

x = 10

m = 5

print(id(x), id(y), id(m))

foo = ['a', 'b', 'c', [1, 2, 3]]
bar = foo
foo.append('d')
print(bar)
print(id(foo), id(bar))

blah = list(foo)  # shallow copy
blah = foo[::]  # shallow copy
print(id(foo), id(blah))
print(foo)
print(blah)
foo.append("wombat")
print(foo)
print(blah)
foo[3].append(99)
print(foo)
print(blah)

baz = deepcopy(foo)
foo[3].append(100000)
print(foo)
print(baz)

flem = foo.copy()
print(id(foo), id(flem))

#  a-z A-Z 0-9 _

_  = "wombat"

__0__ = "do not do this"

print(__0__)


for _ in range(3):
    print("wombats are fun!")

x

burf = None

all_lower_case_with_underscores = "YES!"

# numeric: int bool float complex
# sequence: str bytes list tuple
# mapping: dict set frozenset














