#!/usr/bin/env python


Animal = type('Animal', (), {'run': lambda self: print("hyperambulating")})

Dog = type('Dog', (Animal,), {'bark': lambda self: print("Woof! Woof!")})

d = Dog()
d.bark()
d.run()

class Toad():
    pass

print(type(Toad))
t = Toad()
print(type(t))
