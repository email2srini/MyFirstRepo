#!/usr/bin/env python3

import crayons

def main(name):
    result = crayons.cyan(name, bold = True)
    return result


question = input("what is your name? ")

if question == "Srini":
    print(main(question))
else:
    print(question)
