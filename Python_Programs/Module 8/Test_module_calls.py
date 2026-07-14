#!/usr/bin/env python3
#
# Problem: Chapter 8 class module call Examples
# Files:
#     greeting.py
# 
# Author: instructor
# Date: 25 jun 2025
#
# Note - docstrings are written with "#" to make classroom demonstration easier
#
# import functions from greeting.py

import greeting
#ONLY USE as TO MAKE THE FUNCTION REFERENCE SHORTER
import greeting as adifferentnameforgreeting
#THE NAME OF YOUR MODULE WHEN IMPORTING NEEDS TO BE THE EXACT SAME AS THE NAME OF THE FILE WITHOUT THE .py
import all_the_functions
#ONLY IMPORTING THE SPECIFIED FUNCTION
from all_the_functions import print_course
#ONLY IMPORTING THE SPECIFIED FUNCTION AND CALLING IT hello. as MAKES AN ALIAS
from all_the_functions import hello_greeting as hello
#from all_the_functions import *
from which_course import print_course as pcourse

def hello_greeting ():
    print ("This is the interal greeting")

# call hello_greeting 
greeting.hello_greeting ()           # use this one with greeting and all_the_functions

#adifferentnameforgreeting.hello_greeting ()     # use this one with import greeting as all_the_functions.hello_greeting ()

# what if we have a local funtion
#hello_greeting ()

#all_the_functions.farewell ()

# call print_course
#print_course ("CIST2742")

# call hello_greeting as hello from all_the_functions
#hello ()
"""
# using import *
hello_greeting ()
print_course ("CIST2431")
farewell ()
"""

pcourse ("CIST2742")    # use with from which_course import as
all_the_functions.print_course ("CISTnnnn")   # used with import all_the_functions



