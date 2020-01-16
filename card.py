#!/usr/bin/env python

from dataclasses import dataclass, field
from typing import List, ClassVar
import random
from pprint import pprint


@dataclass
class Card:
    rank: str
    suit: str

    # def __repr__(self):
    #     return f"{self.rank}-{self.suit}"


