#!/usr/bin/env python
from abc import ABCMeta, abstractmethod


print(type(ABCMeta))


class CardBase(metaclass=ABCMeta):

    @abstractmethod
    def draw(self):
        pass
