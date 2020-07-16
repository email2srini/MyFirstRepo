#!/usr/bin/env python3

userinput = input("Please enter something : ")

if isinstance(userinput, str):
    print("you entered a text")
elif isinstance(userinput, int):
    print("you entered an integer")
else:
    print("you entered alphanumeric")
