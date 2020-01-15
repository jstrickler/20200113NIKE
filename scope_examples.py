#!/usr/bin/env python
# from __builtins__ import *
import sys

def print(*args, **kwargs):
    sys.stdout.write("HA HA HA\n")

x = 100

def blurge():
    y = 1000
    name = "Foofy"
    print("x is", x)

    def waaaa():
        print("name is", name)

    return waaaa

f = blurge()
print(type(f))
f()

len = 12

x = "abc"
print(__builtins__.len(x))

