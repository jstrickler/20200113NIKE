#!/usr/bin/env python
from president import President

tr = President(26)

print(tr.first_name, tr.last_name)

attr_wanted = 'party'


print(tr.party)

print(getattr(tr, attr_wanted))

if hasattr(tr, "last_name"):
    print(tr.last_name)

setattr(tr, 'favorite_song', 'Disco Inferno')

print(tr.favorite_song)


def get_full_name(self):
    return f"{self.first_name} {self.last_name}"

setattr(President, 'get_full_name', get_full_name)

print(tr.get_full_name())

print(dir(tr))
print('-' * 60)

for attr in dir(tr):
    if not attr.startswith('_'):
        a_value = getattr(tr, attr)
        if callable(a_value):
            print(a_value())
        else:
            print(attr, a_value)

