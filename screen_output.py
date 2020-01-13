#!/usr/bin/env python

spam = 28
ham = 'wombat'
eggs = 24.90392

print(spam, ham, eggs)

print(spam, ham, eggs, sep=":")

print(spam, ham, eggs, sep=", ")

print(spam)
print(ham)
print(eggs)

print(spam, end="FAZOO")
print(ham, end='')
print(eggs)

import sys

print("HELP HELP HELP!!", file=sys.stderr)

print("HELP HELP HELP!!\n", file=sys.stderr, flush=True)

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip('\n\r')
        print(line)
print()

with open('somejunk.txt', 'w') as junk_out:
    for word in 'battery', 'wombat', 'Wankel rotary engine':
        print(word, file=junk_out)
#        junk_out.write(word + '\n')

#   r   w   a   x
#   rb   wb   ab   xb


word = input("What is the word? ")
print("My word is {}".format(word))

from getpass import getpass

secret_password = getpass("Enter your super secret password: ")
print("your password is", secret_password)


