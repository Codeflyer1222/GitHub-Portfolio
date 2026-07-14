#!/usr/bin/env python3
#
# Problem: try / except demonstration
# Files:
#     try_except_ex.py (this file)
#  
# Author: instructor
# Date: 2 July 2025
#
# This code introduces the use of try except
#
from pathlib import Path
FILENAME = "CustData.txt"
#FILENAME = "alice.txt"

numerator = 5
denominator = 1


#attempt to divide by zero
print (numerator / denominator)
print ("This statement is after the attempt to print 5/0")

#attempt to divide by zero and attempt to open a file that does not exist
try:
    with open ("stupidfile", "r"):
       print ("opened stupid file")
    
    print (numerator / denominator)

except:
    print ("You cannot divide by 0")


#attempt to divide by zero and call out specific exception
try:
    with open ("customer_data.txt", "r"):
       print ("opened stupid file")

    quotient = numerator / denominator
except ZeroDivisionError: 
    print ("You cannot divide by 0")
    print ("This is a 2nd statement")
except FileNotFoundError:
   print ("The file does not exist")
except Exception as err:
        print (f"An error was recieved. Error = {err}")
else:
    print (f"The answer is {quotient}")

# create a path object for the file 
path = Path (FILENAME)

# attempt read of file that does not exist
#contents = path.read_text (encoding='utf-8')

# use try and except to get around the error
try:
    #encoding CHANGES FORMAT OF CODE INSTEAD OF READING AS BYTES BY DEFAULT.
    contents = path.read_text (encoding='utf-8')
except FileNotFoundError:
    print (f"The file {FILENAME} does not exist")
else:
    print ("Was able to open the file")

print ("Last line of try_except example code")
