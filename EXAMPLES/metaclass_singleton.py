#!/usr/bin/env python

class Singleton(type): # <1>
    _instances = {}  # <2>

    def __call__(cls, *args, **kwargs):  # <3>
        if cls not in cls._instances:    # <4>
            cls._instances[cls] = super().__call__(*args, **kwargs)  # <5>

        return cls._instances[cls]   # <6>


class ThingA(metaclass=Singleton):   # <7>
    pass


class ThingB(metaclass=Singleton):   # <7>
    pass


ta1 = ThingA()  # <8>
ta2 = ThingA()
ta3 = ThingA()

tb1 = ThingB()
tb2 = ThingB()
tb3 = ThingB()

for thing in ta1, ta2, ta3, tb1, tb2, tb3:
    print(type(thing).__name__, id(thing))  # <9>
