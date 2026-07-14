#!/usr/bin/env python3
# Problem: Registration Form
# Files:
# BrownS_RegistrationForm.py
#
# Author: Samuel Brown
# Date: 21-JAN-2026
#
# provide comments for each section of code

#Prompt
print("Registration Form\n\n")
#User's First Name
#input function returns a string value unless you use the int() function in front.
FirstName = input("First Name:\t")

#User's Last Name
LastName = input("Last Name:\t")

#User's Birth Year
BirthYear = input("Birth Year:\t")

#Welcome message
print("\nWelcome " + FirstName + " " + LastName + "!")

#end message
print("Your registration is complete")

#temporary password
print("Your temporary password is: " + FirstName + "*" + BirthYear)
