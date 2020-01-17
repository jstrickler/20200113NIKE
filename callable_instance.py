#!/usr/bin/env python


class Spam():

    def __call__(self, value):
        return value * 2

s = Spam()

print(s(5))
print(s("wow!"))
