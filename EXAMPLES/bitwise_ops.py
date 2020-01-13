#!/usr/bin/env python

a = 0b10101010  # <1>
b = 0b11110000

c = a & b  # <2>
print("  {:08b}".format(a))
print("& {:08b}".format(b))
print("  --------")
print("  {:08b}".format(c))
print()

c = a | b # <3>
print("  {:08b}".format(a))
print("| {:08b}".format(b))
print("  --------")
print("  {:08b}".format(c))
print()

c = a ^ b # <4>
print("  {:08b}".format(a))
print("^ {:08b}".format(b))
print("  --------")
print("  {:08b}".format(c))
print()

c = ~a # <5>
print(" ~ {:09b}".format(a))
print("   {:09b}".format(c))
print()

c = a >> 1 # <6>
print("{:08b} >> 1".format(a))
print("{:08b}".format(c))
print()

c = a >> 3 # <7>
print("{:08b} >> 3".format(a))
print("{:08b}".format(c))
print()

c = a << 1 # <8>
print("{:012b} << 1".format(a))
print("{:012b}".format(c))
print()

c = a << 3 # <9>
print("{:012b} << 3".format(a))
print("{:012b}".format(c))
print()
