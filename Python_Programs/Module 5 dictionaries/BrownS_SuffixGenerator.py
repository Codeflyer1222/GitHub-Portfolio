#!/usr/bin/env python3
#
# Problem: Rock, Paper, or Scissors
# Files:
# N/A
#
# Author: Samuel Brown
# Date: 14 FEB 2026
#
# provide comments for each section of code

#Title of program
print("Suffix Generator\n")

#the User's input number
UserNmbr = int(input("Enter a number: "))

#Uses modulo to check if the remainder equals the following numbers in parentheses to see if the 
#last two digits end in 11, 12, or 13.
if UserNmbr % 100 in (11, 12, 13):
    #will add th to the user's number
    suffix = "th"
#Uses modulo to see if remainder equals 1 to see if the User's last digit is one
elif UserNmbr % 10 == 1:
    #adds the st suffix to the User's number
    suffix = "st"
#Uses modulo to see if remainder equals 2 to see if the User's last digit is two
elif UserNmbr % 10 == 2:
    suffix = "nd"
#Uses modulo to see if remainder equals 3 to see if the User's last digit is three
elif UserNmbr % 10 == 3:
    suffix = "rd"
#every other number not fitting into any other category describted above will get the suffex th
else:
    suffix = "th"

#print to screen the user's number and the suffix
print(f"\n {UserNmbr}{suffix}")