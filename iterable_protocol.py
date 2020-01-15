#!/usr/bin/env python

class Wacky:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        self.count -= 1
        return "blug"


w = Wacky(3)
for i in w:
    print(i)
print('-' * 60)u
w = Wacky(10)
for thing in w:
    print(thing)
