#!/usr/bin/env python3

# create a small string

tinystring = "I am taking python class"
splittinystring = tinystring.split()

print(splittinystring)

listofstrings = ["this", "24", "frames", "movie", "is", "great"]
attachstrings ="-".join(listofstrings)

print(attachstrings)

newstring = "testing fstring"
newerstring = "more testing"

fstring = f'{tinystring} "$$" {newstring} "$$" {newerstring}'
print(fstring)

# let me see...
