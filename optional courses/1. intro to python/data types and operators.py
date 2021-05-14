# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:33:41 2021

@author: yuqing
"""
# Write an expression that calculates the average of 23, 32 and 64.
# Place the expression in this print statement.
print((23 + 32 + 64)/3)

# Fill this in with an expression that calculates how many tiles are needed.
print(9*7 + 5*7)
# Fill this in with an expression that calculates how many tiles will be left over.
print(17*6 - (9*7 + 5*7))

print(9**3)

print(9 % 2) # remainder
print(7//2)

# ---------
# data types
# -----------

# strings
my_string = 'this is a string!'
my_string2 = "this is also a string!!!"
print(my_string + my_string2)
print(my_string * 5)

# quiz 1
# TODO: Fix this string!
# ford_quote = 'Whether you think you can, or you think you can't--you're right.'
# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'

# TODO: Fix this string!
ford_quote = "Whether you think you can, or you think you can't--you're right."

# quiz 2
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = "#todo: calculate how long this name is"

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
ame_length = len(given_name) + len(middle_names) + len(family_name) + 2


# quiz 3
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

print (username + " accessed the site " + url + " at " + timestamp + ".")



# ---
# integers and floats

x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0

# ---
# booleans, comparisons operators, and logical operators

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
if (san_francisco_pop_density > rio_de_janeiro_pop_density):
    print (True)
else:
    print (False)


# type conversation

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales)  #convert the type back!!
print("This week's total sales: " + weekly_sales)

# String Methods
len("this")
type(12)
print("Hello world")

# more methods
my_string = "yuqing"

# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# and try them out here

my_string.capitalize()
my_string.encode()
my_string.format()
my_string.isalpha()
my_string.islower()
my_string.istitle()
my_string.casefold()
my_string.endswith()
my_string.format_map()
my_string.isdecimal()
my_string.isnumeric()
my_string.isupper()
my_string.center()
my_string.expandtabs()
my_string.index()
my_string.isdigit()
my_string.isprintable()
my_string.join()
my_string.count()
my_string.find()
my_string.isalnum()
my_string.isidentifier()
my_string.isspace()
my_string.ljust()

# another important string function
new_str = "The cow jumped over the moon."
new_str.split()
new_str.split(' ', 3)
new_str.split('.')
new_str.split(None, 3)

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!

print("Verse has a length of {} characters.".format(len(verse)))
print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))
print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))
print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))

# another way

message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."

length = len(verse)
first_idx = verse.find('and')
last_idx = verse.rfind('you')
count = verse.count('you')

print(message.format(length, first_idx, last_idx, count))



























