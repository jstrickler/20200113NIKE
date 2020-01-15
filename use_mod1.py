#!/usr/bin/env python
import sys
from nike.cis import niketools

niketools.jump()
niketools.run()

for path in sys.path:
    print(path)

