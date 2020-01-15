#!/usr/bin/env python

def hello_world():
    print("Hello, world")

hello_world()

def c2f(c):
    return (c * (9/5)) + 32

for i in -40, 0, 37, 100:
    c2f(c=i)


def wacky(p1: int, p2: int) -> float:
    print("p1:", p1)
    print("p2:", p2)

x = wacky(1, 2)
y = wacky('a', 'b')
print(x, y)

def blurch(p1, p2='wombat', *p3, file_name='barf.txt', **p4):
    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)
    print("file_name:", file_name)
    print("p4:", p4)
    print()

blurch('a', 'b', file_name="")
blurch('b', 'a', 'c', 'm', 99, ['carbuncle', 'ocelot'], file_name="fred")
blurch('foo', file_name='bar.txt')
blurch('weasel', disease="black plague", weapon="rat")


def process_file(*, folder=".", file_name="init.txt", order="forward"):
    pass


def generic(*args, **kwargs):
    pass


generic()
generic(1, 2)
generic(1, 2, foo="fred", bar="barney")


# def will_this_work(p1, p2, /, p3, p4):
#     pass
#
# will_this_work(1, 2, p3=3, p4=4)


def foo(*, file_name=None, folder=None):
    if (file_name is None) or (folder is None):
        raise ValueError("Missing args...")

foo()
