#!/usr/bin/env python
from contextlib import closing


# mary_in = open(...)
with open('DATA/mary.txt') as mary_in:
    pass

class Foo:

    def __enter__(self):
        print("ENTERING")

    def __exit__(self, *_):
        print("EXITING")
        print("exit info:", _)
        return True

with Foo():
    print("In the block...")
    raise ZeroDivisionError('ugh')
    print("Huh....")


with closing(some_object) as thing:
    # use thing.....

