#!/usr/bin/env python3
#
# Problem: writing standard text file format
# Files:
#     txtfile_write.py (this file)
#     
#  
# Author: instructor
# Date: 2 July 2025
#
# This code demonstrates writing to a text file
#
from pathlib import Path

FILENAME="afile.txt"
FILENAME2="bfile.txt"

# write one statement to a text file
path = Path (FILENAME)
path.write_text ("I dislike programming")

# write multiple statements to a text file
# build the 'structure' to write
path = Path (FILENAME2)
sentence = "This is the first line \t"
sentence += "This is the second line \t"
sentence += "This is the third line \t"
sentence += "This is the last line \t"

path.write_text (sentence)

print ("Last line of txtfile_write code")