# Create a list of cars with atleast 5 elements in it
# create a list of names
# print out items from the third index of each list
# print out the slice containing items from cars at indices 2-4(inclusive)
# print out the slice containing items from names at indices 0-2 (non inclusive)
# create a blank list named combined
# use the append method to add the cars in to list
# use the extend method to add the names in to the list
# print out 2 cars and 2 names from combined list

#!usr/bin/env python 3

cars = ["0Sedan", "1Hatchback", "2Pickup Truck", "3SUV", "4Electric"]
names = ["0BMW", "1Honda", "2Ford", "3Toyota", "4Tesla"]

print("These are cars from 3rd index: ", cars[3:])
print("These are names from 3rd index: ", names[3:])

print("These are cars sliced frm indices 2-4(inclusive): ", cars[1:4])
print("These are names sliced frm indices 2-4(inclusive): ", names[1:4])

combined = []
combined.append(cars)
print("Used append to add cars to new list called combined: ", combined)

combined.extend(names)
print("Used extend to add names: ", combined)
# The result from this command is:
# Used extend to add names:  [['0Sedan', '1Hatchback', '2Pickup Truck', '3SUV', '4Electric'], '0BMW', '1Honda', '2Ford', '3Toyota', '4Tesla']
# Let's count them:             0 [0]       [1]             [2]            [3]     [4]          1        2         3        4           5
# So combined[3:] == ['2Ford', '3Toyota', '4Tesla']
# And combined[5] == '4Tesla'
# And combined[5][3:] == 'sla'
print("Here are 2 cars and 2 names from combined list: " , combined[0][3:], combined[1:3])


# Let me run it and see where you are going wrong here



