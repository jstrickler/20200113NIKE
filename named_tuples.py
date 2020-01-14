#!/usr/bin/env python
from person import Person

p1 = Person('Bill', 'Gates', 'Microsoft', '1955-10-28')

print(p1)
print(p1.first_name, p1.last_name)

x = p1._replace(first_name="Melinda")
print(x)

print(p1._asdict())
print(p1._fields)

# last_names = [x.last_name for x  in list_of_named_tuples]

