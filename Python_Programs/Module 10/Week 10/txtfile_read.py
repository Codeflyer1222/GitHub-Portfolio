#!/usr/bin/env python3
#
# Problem: reading standard text file format
# Files:
#     txtfile_read.py (this file)
#     pi_million_digits.txt - text file to read (from book data)
#  
# Author: instructor
# Date: 2 July 2025
#
# This code demonstrates reading from a text file
# This code can be found in Matthes, E. (2023). Python Crash Course. no starch press. p. 187
#
from pathlib import Path

FILENAME="pi_million_digits.txt"
BDAY="120372"
#BDAY="031763"

path = Path (FILENAME)

if path.exists ():
    contents = path.read_text ()
   # print (contents)
else:
    print (f"The file {FILENAME} does not exist")

if BDAY in contents:
    print ("Your birthday appears in the first million digits of pi")
else:
    print ("Your birthday does not appear in the first million digits of pi")

print ("Last line of txtfile_read code")