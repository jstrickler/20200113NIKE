#!/usr/bin/env python

class Blag:   # (object)
    # constructor
    def __init__(self, number):
        self._number = number

    # getter method
    def get_number(self):
        return self._number

    # getter property
    @property
    def number(self):
        return self._number

    # setter property
    @number.setter
    def number(self, value):
        if isinstance(value, int):
            self._number = value
        else:
            raise TypeError("number must be an int")


    @property
    def fungus(self):
        return self._fungus

    @fungus.setter
    def fungus(self, value):
        self._fungus = value

    @property
    def blurch(self):
        return 42

    def doit(self):
        print("OK OK OK")

b = Blag(123)   # Barf b = new Barf();
print(b)
print(Blag.get_number(b))
print(b.get_number())
print(b.number)
print(b.number * 10)
b2 = Blag(456)
print(b2)

try:
    b2.number = "abc"
except TypeError as err:
    print(err)


