#!/usr/bin/env python
from typing import Union, Any, Iterable

Number = Union[int, float]

def spam(foo: Number ) -> float:
    return foo * 10

def ham(bar: Any) -> None:
    pass

def ham(blah: Iterable) -> List:
    pass



