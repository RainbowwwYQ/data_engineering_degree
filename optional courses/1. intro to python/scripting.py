# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:23:08 2021

@author: yuqing

Python Installation and Environment Setup
Running and Editing Python Scripts
Interacting with User Input
Handling Exceptions
Reading and Writing Files
Importing Local, Standard, and Third-Party Modules
Experimenting with an Interpreter

"""

# Quiz: Generate Messages

# Hi [insert student name],

# This is a reminder that you have [insert number of missing assignments] 
# assignments left to submit before you can graduate. Your current grade is 
# [insert current grade] and can increase to [insert potential grade] if you 
# submit all assignments before the due date.

names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))

    
# Errors And Exceptions

# handling errors

# try:
#     # some code
# except ValueError:
#     # some code
# except KeyboardInterrupt:
#     # some code

def party_planner(cookies, people):
    
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
        
    except ZeroDivisionError:
        
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")

    return(num_each, leftovers)

# raise error message

# try:
#     # some code
# except Exception as e:
#    # some code
#    print("Exception occurred: {}".format(e))


# reading a file

f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()

# Writing to a File

f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()

# Too Many Open Files
files = []
for i in range(10000):
    files.append(open('some_file.txt', 'r'))
    print(i)

# Python provides a special syntax that auto-closes a file for you once you're finished using it

with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()

# Quiz Solution: Flying Circus Cast List

def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
    
# quiz 2

user_list = []  
list_sum = 0
for i in range(10):
    userInput = int(input("Enter any number: "))
    try:
        user_list.append(userInput)
        if userInput % 2 == 0:
            list_sum += userInput
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))

# Importing Local Scripts

# demo.py

import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)


# useful_functions.py

def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()
    



















