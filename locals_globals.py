#!/usr/bin/env python


x = 100

def ham():
    y = 42
    print("HI")
    print(locals())


g = globals()

print(g['x'])
g['ham']()

print(globals())


g['color'] = 'blue'

print(color)

print(type(g))

g['bark'] = lambda: print("woof woof")

bark()

