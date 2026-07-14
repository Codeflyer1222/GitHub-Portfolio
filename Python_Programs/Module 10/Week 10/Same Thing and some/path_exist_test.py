#!/usr/bin/env python3
#
# Problem: pathlib example
# Files:
#     path_exist_test.py (this file)
#     words.txt - text file to read
#  
# Author: instructor
# Date: 2 July 2025
#
# This code demonstrates the use of pathlib from Path Module
#
from pathlib import Path
import json
"""
# Configure the path to the file
# Print out the attributes and methods of the "path" object
#
path = Path ('words.txt')
print (f"The path to the words.txt file {path.cwd ()} \n The variable path is of type {type (path)}")
for element in dir (path):
    print (element)

#the following will cause an error if the file does not exist
contents = path.read_text ()
print (f"The variable data type {type (contents)} and the data contains: \n{contents}")

# Validate file exists and print data in the file
if path.exists ():
    contents = path.read_text ()
    print (f"The variable data type {type (contents)} and the data contains: \n{contents}")
else:
    print (f"The file words.txt does not exist")

# note - typingsentences has a blank line at the bottom
# use rstrip to strip out blank lines
#path = Path ('typingsentences.txt')
print (f"\n\nThe path to the typingsentences.txt file {path.cwd ()}")

if path.exists ():
   contents = path.read_text ()
#   contents = contents.rstrip()
#   contents = path.read_text().rstrip() # <== same as two statements above
   print (f"The variable data type {type (contents)} and the data contains: \n{contents}")
else:
    print (f"The file typingsentences.txt does not exist")

# using the json library <-- different formatted file
path = Path ('username3.json')
print (f"\n\nThe path to the username.txt file {path.cwd ()}")

if path.exists ():
    contents = path.read_text ()
    username = json.loads (contents)
    print (f"Welcome back, {username}!")
else:
    username = input ("what is your name? ")
    contents = json.dumps (username)
    path.write_text (contents)
    print (f"We'll remember you when you come back, {username}!")

# example of an absolute path
path = Path ('FileInDifferentDir.txt')
#path = Path ('C:/Users/gvolz/FileInDifferentDir.txt')
#path = Path ('C:\\Users\\gvolz\\FileInDifferentDir.txt')
print (f"\n\nThe path to the FileInDifferentDir.txt file {path.cwd ()}")

if path.exists ():
    contents = path.read_text ()
#    contents = contents.rstrip()
#    contents = path.read_text().rstrip() <== same as two statements above
    print (f"The variable data type {type (contents)} and the data contains: \n{contents}")
else:
    print (f"The file FileInDifferentDir.txt does not exist")

print ("Last line of code")
"""