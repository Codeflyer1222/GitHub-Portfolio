#!/usr/bin/env python3
#
# Problem: provide an example of using splitlines function
# Files:
#     pi_read.py (this file)
#     pi_digitis.txt - text file to read
#  
# Author: instructor
# Date: 2 July 2025
#
#
from pathlib import Path

# create path object describing the pi_digits file
path = Path ('pi_digits.txt')
contents = path.read_text().rstrip ()    # read the file striping additional lines
# the code statement above is the concatenation of the two following statements
#contents = path.read_text()
#contents = contents.rstrip ()
"""
lines = contents.splitlines ()
for line in lines:
    print (line)

lines = contents.splitlines ()
pi_string = ''
for line in lines:
    pi_string += line
#    pi_string += line.lstrip ()

print (pi_string)
print (len (pi_string))

#print (contents)
"""