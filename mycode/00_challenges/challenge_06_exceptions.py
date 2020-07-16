#!/usr/bin/python3

# Create a function that takes a required argument of a list, and an optional parameter of an integer


def user_input(mandatory, optional=10):
    for item in mandatory:
        try:
            result = item / optional
            print(f"result is {result}")
        except TypeError as err:
            print(err)
            print(f"your item {item} is not divisible by {optional}")


mandatory = [50, "cats", "lizards", 7, "fish", 300]
optional = input("Please enter an optional integer: ")
user_input(mandatory)


# Iterate through each item of the list
# Use a try/except block to "try" to divide each item by your optional integer parameter
# If there is a TypeError, handle it by printing out the value of the error (err) and also printing "Your item ____ is not divisible by ____ " (fill in with item of list, and optional integer)
# Execute the function

# Use the list below (or one like it) to accomplish this task
