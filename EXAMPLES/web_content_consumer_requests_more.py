#!/usr/bin/env python
from pprint import pprint
from dataclasses import make_dataclass
import sys
import requests
from keyword import kwlist as KWLIST


BASE_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'  # <1>

API_KEY = 'b619b55d-faa3-442b-a119-dd906adc79c8' # <2>

def main(args):
    if len(args) < 1:
        print("Please specify a search term")
        sys.exit(1)

    searchterm = args[0]

    data = get_raw_data(searchterm)

    entries = parse_entries(data, searchterm)

    display_entries(entries)


def get_raw_data(searchterm):
    try:
        response = requests.get(
            BASE_URL + searchterm,
            params={'key': API_KEY},
        )  # <3>
    except requests.HTTPError as err:
        print(err)
    else:
        if response.status_code == requests.codes.OK:
            return response.json()
        else:
            print("Sorry, HTTP response", response.status_code)
            exit()


def parse_entries(data, searchterm):
    # uncomment the next to lines to see raw data:
    # pprint(data)
    # print('-' * 60)
    object_list = []
    for i, entry in enumerate(data, 1): # <5>
        if isinstance(entry, dict):
            field_names = tuple(k + "_" if k in KWLIST else k for k in entry.keys())
        class_name = f"{searchterm}{i:02d}"
        globals()[class_name] = make_dataclass(class_name, field_names)
        n = globals()[class_name](*entry.values())
        object_list.append(n)

    return object_list

def display_entries(entries):
    for entry in entries:
        print(entry.hwi['hw'].upper(), end=' ')
        print(f"({entry.fl})")
        for line in entry.shortdef:
            print(line)
        print()


if __name__ == '__main__':
    main(sys.argv[1:])
