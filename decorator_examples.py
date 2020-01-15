#!/usr/bin/env python
from datetime import datetime
from functools import wraps
import logging

logging.basicConfig(filename="deco.log", level=logging.DEBUG)

def nuller(old_func):
    def null(*args, **kwargs):
        pass

    return null


@nuller
def some_function():
    print("Hi Mom!!")

some_function()


# @foo
# def bar():
#     pass
#
# bar = foo(bar)

# @spam(PARAM)
# def ham():
#     pass
#
# ham = spam(PARAM)(ham)
#


def timestamp(old_func):

    @wraps(old_func)
    def wrapper(*args, **kwargs):
        print(datetime.now().ctime())
        result  = old_func(*args, **kwargs)
        return result

    return wrapper

@timestamp
def spam():
    print("calling spam()")

@timestamp
def ham():
    print("calling ham()")

spam()
spam()
ham()
spam()
ham()
print(spam.__name__, ham.__name__)
print(id(spam), id(ham))



def timestamp2(dest, animal, number):

    def real_decorator(old_func):

        @wraps(old_func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.now().ctime()
            if dest == 'stdout':
                print(timestamp)
            else:
                logging.debug(timestamp)
            result  = old_func(*args, **kwargs)
            return result

        return wrapper

    return real_decorator

@timestamp2("stdout", "wombat", 36)
def ocelot():
    print("calling spam()")

@timestamp2("logger", "weasel", 42)
def weasel():
    print("calling ham()")

ocelot()
ocelot()
weasel()
ocelot()
weasel()
