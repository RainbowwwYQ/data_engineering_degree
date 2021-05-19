# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:10:00 2021

@author: yuqing

Defining Functions
Variable Scope
Documentation
Lambda Expressions
Iterators and Generators

"""

# an example
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

cylinder_volume(10, 3)


# Print vs. Return in Functions

# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))

# Default Arguments

def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2

cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name

# Quiz: Population Density Function

def population_density(population, land_area):
    return population/land_area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))


# Quiz: readable_timedelta

def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))

# Variable Scope



# This will result in an error

# def some_function():
#     word = "hello"

# print(word)



# This works fine

# def some_function():
#     word = "hello"

# def another_function():
#     word = "goodbye"

# # This works fine
# word = "hello"

# def some_function():
#     print(word)

# some_function()


# Documentation

def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area

def population_density(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT: 
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area


# Quiz: Write a Docstring

def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days."""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days.

    Args:
        days (int): number of days to convert
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

def readable_timedelta(days):
    """
    Return a string of the number of weeks and days included in days.

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)


# Lambda Expressions

def multiply(x, y):
    return x * y

# in the same way

multiply1 = lambda x, y: x * y

multiply1(4, 7)

# Quiz: Lambda with Map

# filter(func,iterable)和map(func,iterable)都可以通过其特性对可迭代对象进行过滤，
# 其中filter只返回对象中条件为真的元素，而map对象会返回所有元素对应的函数值
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

# ---
# map() is a higher-order built-in function that takes a function and iterable as inputs, 
# and returns an iterator that applies the function to each element of the iterable. 
# The code below uses map() to find the mean of each list in numbers to create the list averages
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)


# Quiz: Lambda with Filter

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)

# ---
# filter() is a higher-order built-in function that takes a function and iterable 
# as inputs and returns an iterator with the elements from the iterable for which 
# the function returns True. The code below uses filter() to get the names in cities 
# that are fewer than 10 characters long to create the list short_cities.

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)




