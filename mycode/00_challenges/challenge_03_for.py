# Create a list of your favorite foods (at least 5 items)
# Iterate through that list with a for loop
# For each item in your list, print " I can't wait to eat some ____!"

#!usr/bin/python3

# Create a list of your favorite foods (at least 5 items)
foods = ["rice", "veggies", "fruits", "nuts", "lentils"]

# Iterate through that list with a for loop
for favorite in foods:
    print("I can't wait to eat some" + " " + favorite, end = ":")
    if favorite =="rice":
        print("because i can't stay without it")
    elif favorite == "veggies":
        print("because they are so healthy")
    elif favorite =="fruits":
        print("yummy!")
    elif favorite == "nuts":
         print("crunchy!")
    elif favorite == "lentils":
        print("protein")
