#!/usr/bin/env python
from pprint import pprint
from dataclasses import make_dataclass
import sys
import requests


BASE_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'  # <1>

API_KEY = 'b619b55d-faa3-442b-a119-dd906adc79c8' # <2>

KEYWORDS = frozenset('def class if else elif with'.split())

def main(args):
    if len(args) < 1:
        print("Please specify a search term")
        sys.exit(1)

    response = requests.get(
        BASE_URL + args[0],
        params={'key': API_KEY},
    )  # <3>

    if response.status_code == requests.codes.OK:
        # pprint(response.content.decode())
        print('-' * 60)
        data = response.json()  # <4>
        pprint(data)
        print('-' * 60)
        class_name = "WordDict"
        for i, entry in enumerate(data): # <5>
            if isinstance(entry, dict):
                field_names = tuple(k + "_" if k in KEYWORDS else k for k in entry.keys())
                print(field_names)
                NewClass = make_dataclass(class_name, field_names)
                n = NewClass(*entry.values())
                print(n)
                print(n.fl)
                print(n.ins)
                print(n.ins[0]['if'])
                print(n.meta['uuid'])
                print(n.def_)
            else:
                print(entry)

    else:
        print("Sorry, HTTP response", response.status_code)


if __name__ == '__main__':
    main(sys.argv[1:])
