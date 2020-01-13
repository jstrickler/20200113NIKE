#!/usr/bin/env python
import os

print(os.environ['HOME'])

print(os.getenv("LOGNAME"))

print(os.getenv("WOMBAT", 'koala'))
