#!/usr/bin/env python

i = 0
while i < 3:
    print("boogie-woogie")
    i += 1
print()

# while True:
#     name = input("What is your name (q to quit)? ")
#     if name == 'q':
#         break
#     if name == '':
#         continue
#     print("Hello, {}".format(name))


fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

for f in fruits:
    print(f.upper())
print()
print("f is", f)

target = 'x'
for f in fruits:
    #   f[0] == 'x'
    if f.startswith(target):
        print(f)
        break
else:
    print(target, "not found")

