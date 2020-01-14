#!/usr/bin/env python

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(sorted(nums))
print(sorted(nums, reverse=True))

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1:", f1, '\n')

def ignore_case(s):
    return s.lower()

f2 = sorted(fruits, key=ignore_case)
print("f2:", f2, '\n')

f3 = sorted(fruits, key=str.lower)
print("f3:", f3, '\n')

f4 = sorted(fruits, key=lambda s: s.lower())
print("f4:", f4, '\n')

#  lambda args ... : return-value

f5 = sorted(fruits, key=len)
print("f5:", f5, '\n')

def custom1(e):
    return len(e), e.lower()

f6 = sorted(fruits, key=custom1)
print("f6:", f6, '\n')

f7 = sorted(fruits, key=lambda e: (len(e), e.lower()))
print("f7:", f7, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print()

for person in sorted(people, key=lambda e: e[3]):
    print(person)



