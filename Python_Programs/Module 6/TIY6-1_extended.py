#!/usr/bin/env python3
#
# Problem: TIY 6-1 extended
# Files:
#     CIST2742_C6_TIY_6-1.py
# 
# Author: instructor
# Date: 28 Sep 2025
#
# Using the dictionary created TIY 6-1
#
# Person list -- ADDED
person_list = []

# The template of the person dictionary data
person_data_dict = {
    'first_name' : "",
    'last_name' : "",
    'age' : 0,
    'city' : ""
}

# ADDED 
# We do not know how to stop a loop, yet
# Therefore we will take 3 names

for index in range (3): 

    # gather information from user
    person_firstname = input ("Enter the 1st name: ")
    person_lastname = input ("Enter the last name: ")
    person_age = int (input ("Enter the person's age: "))
    person_city = input ("Enter the person's city: ")

    # set the dictionary fields
    person_data_dict ['first_name'] = person_firstname
    person_data_dict ['last_name'] = person_lastname
    person_data_dict ['age'] = person_age
    person_data_dict ['city'] = person_city

    # add the new person to the list
    #person_list.append (person_data_dict)
    person_list.append ({'first_name' : person_firstname, 
                        'last_name' : person_lastname, 
                        'age' : person_age, 
                        'city' : person_city,
                        })
                        
    print ("\n Add another name \n")

# print the data
for index in range (3):
    print ("The ", index, "name entered:", person_list [index])