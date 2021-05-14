# -*- coding: utf-8 -*-
"""
Created on Thu May 13 22:05:57 2021

@author: yuqing
"""

# lists
# Lists can contain any mix and match of the data types you have seen so far.

list_of_random_things = [1, 3.4, 'a string', True]
list_of_random_things[0]
list_of_random_things[-2]

# Slice and Dice with Lists
list_of_random_things[1:2]
list_of_random_things[:2]
list_of_random_things[1:]

'isa' in 'this is a string'

# mutability and order
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'

# However, the following does not work:
# greeting = "Hello there"
# greeting[0] = 'M'

# functions
len(list_of_random_things)
max()
min()
sorted()

new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)

# tuples:  immutable ordered sequences of elements
# They are often used to store related pieces of information

location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))


# sets: mutable unordered collections of unique elements
# One application of a set is to quickly remove duplicates from a list.

fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)

# distionary:  a mutable data type that stores mappings of unique keys to values.

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3

print("carbon" in elements)
print(elements.get("dilithium"))
# get looks up values in a dictionary, 
# but unlike square brackets, get returns None 
# (or a default value of your choice) if the key isn't found.

# quiz 1:

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai': 17.8,
              'Istanbul': 13.3,
              'Karachi': 13.0,
              'Mumbai': 12.5}

# or
population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}


# compound data structure
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
print(elements)

# quiz

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
print(elements)


# quiz

# count unique words

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, "\n")

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to set to get unique words
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique)



# verse distionary

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1]) 





