#!/usr/bin/env python


def strip_nl(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')


gen = strip_nl('DATA/mary.txt')
for line in gen:
    print(line)


def beer(min_len):
    yield "IPA"
    yield "Lager"
    yield "Sour"
    yield "Alembic"
    for stuff in "stout", "bitter", "shandygaff":
        if len(stuff) > min_len:
            yield stuff

beer_gen = beer(1)
for b in beer_gen:
    print(b)




