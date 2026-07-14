#!/usr/bin/env python3
#
# Problem:C7 input examples
# Files:
#     class_ex_input.py
# 
# Author: instructor
# Date: 25 feb 25
#
# simple question

QUESTION = "What color is a rose? "
color = input (QUESTION)
#type() WILL RETURN STRING B/C INPUT DEFAULT IS STRING
print (color, '"is of type "', type(color))

# gathering integers and float values
num_roses = int (input ("How many roses do you have? "))
price_roses = float (input ("What is the price of a dozen roses? "))
print (f"The number of roses: {num_roses} ( {type (num_roses)} ) \nThe cost of roses: ${price_roses:.2f} ( {type (price_roses)} )")

# gathering both string and integer value
num2_roses = input ("How many roses do you have? ")
rose_count = int (num2_roses)
#           STRING              INT 
print (type (num2_roses), type (rose_count))

# Reading multiple pieces of information
# each element, digit and spaces, are identified as elements of the list
num_list1 = []
num_list1  = list (input ("Enter a list of numbers "))
print ("numbers1: ", num_list1 )

# spaces are used as delimiters
#.split USES SPACES TO SEPERATE NUMBERS BY DEFAULT
num_list2 = list (input ("Enter a list of numbers ").split())
print ("numbers2: ", num_list2 )

# define the delimiter value as , (comma)
num_list3 = list (input ("Enter a list of numbers ").split(","))
print ("numbers3: ", num_list3 )

# example using character strings
fruits = list (input ("Enter a list of fruits ").split ())
vegetables = list (input ("Enter a list of vegetables ").split ())
print ("fruits", fruits)
print ("vegetables", vegetables)

# add the vegetables to the fruits list
for vegetable  in vegetables :
    fruits.append (vegetable)

# print both lists
print ("fruits and vegetables: ", fruits )
print ("vegetables: ", vegetables )

# the challenge with numbers is changing the input to int
# the following causes an error
# the error is caused because the .split method is used on a string and returns a list
num_list_attempt = list (int (input ("Enter a list of integer numbers ").split()))
print (" the list: ", num_list_attempt, "\n The type of the list is ", type (num_list_attempt))


# To gather integer values use the map function
#map() function fixes error. IT TAKES 2 ARGUMENTS, THE INT, AND THE INPUT. IT RETURNS A MAP TYPE/MAP OBJECT CONCATENER
num_list1 = list (map (int, input ("Enter a list of integer numbers ").split()))
print ("integer numbers: ", num_list1, " type --", type (num_list1 [0]) )

num_list2 = list (map (float, input ("Enter a list of floating point numbers ").split()))
print ("float number: ", num_list2, " type --", type (num_list2 [0])  )

# map example transforming strings to int
string_digits = [ '1', '2', '3', '4', '5']
print ("The initial values: ", string_digits)

int_digits = map (int, string_digits)
int_digits_list = list (int_digits)
print ("The type of int_digits: ", type (int_digits))
print ("The mapped values: ", int_digits_list)

# use direct list
#map() IS NOT SUBSCRIBABLE/INDEXED LIKE A LIST HERE
int_digits2 = map (int, ['8', '7', '6'])

# The return value from map is of type map; maps are not subscribable
# 1st print error message
print ("The type of an element of int_digits: ", type (int_digits2[0]))
print ("The mapped values: ", int_digits2)
"""
