#!/usr/bin/env python

name = "Chris Hemsworth"

#          0    1    2    3    4     5
#         -6   -5    -4   -3   -2    -1
values = ['a', 'b', 'c', 'd', 'e', 'f']

print(name[0], name[8])
print(values[0], values[3])

print(name[-1], values[-1])
print(name[-1], name[len(name)-1])

print(len(name), len(values))


print(values[0:3], values[:3])

#  [start:stop]  [:stop]  [start:]  [:]
#  [::step]

print(name[6:9])

print(name[:5])

print(name[-5:])

x = [1, 2, 3]
x.append(42)
print(x)
y = [8, 9, 10]
x.extend(y)
print(x)

x.insert(0, 888)
x.insert(5, 97)
print(x)

del(x[5])
x.remove(888)
a = x.pop()
b = x.pop(4)
print(x)
print(a, b)






