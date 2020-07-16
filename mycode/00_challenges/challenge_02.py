#!/usr/bin/env python3
  
#Lists and Dictionaries


# Create a dictionary with 2 keys, pets and movies

dictionary = {"pets", "movies"}
print(dictionary)

# Have the value of pets be a list of dictionaries with keys of "type" and "name"
dictionary1 = {"pets":[{"type":"a","name":"a1"}]}
print(dictionary1)

# Have the value of movies be a list of dictionaries with keys of "rating" and "name"
dictionary2 = {"movies":[{"rating":"r1", "name":"n1"}]}
print(dictionary2)

# pets and movies should have 3 items each in them
dictionary3 ={"pets":[{"type":"a", "name":"p1"}, {"type":"b", "name":"p2"}, {"type":"c", "name":"p3"}] , "movies":[{"rating":"a", "name":"m1"}, {"rating":"b", "name":"m2"}, {"rating":"c", "name":"m3"}]}

print(dictionary3)
# print out 2 pets with their type and name
print(dictionary3["pets"][0]["type"])
print(dictionary3["pets"][1])

# print out 1 movie with its rating and name
print(dictionary3["movies"][0])
print(dictionary3["movies"][1])
