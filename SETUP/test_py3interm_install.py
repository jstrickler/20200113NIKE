#!/usr/bin/env python
try:
    import paramiko
except ImportError as err:
    print("paramiko not installed", err)
else:
    print("paramiko installed OK")

try:
    import pylint
except ImportError as err:
    print("pylint not installed", err)
else:
    print("pylint installed OK")

try:
    import singledispatch
except ImportError as err:
    print("singledispatch not installed", err)
else:
    print("singledispatch installed OK")

try:
    import lxml.etree as ET
except ImportError as err:
    print("lxml not installed", err)
else:
    print("lxml installed OK")

try:
    import requests
except ImportError as err:
    print("requests not installed", err)
else:
    print("requests installed OK")
try:
    import dateutil
except ImportError as err:
    print("dateutil not installed", err)
else:
    print("dateutil installed OK")


