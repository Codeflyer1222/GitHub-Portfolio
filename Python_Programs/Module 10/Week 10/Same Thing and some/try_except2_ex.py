#!/usr/bin/env python3
#
# Problem: Ctry except examples
# Files:
#  try_except2_ex.py (this file)
# 
# Author: 
# Date: 9 July 2025
#

# define imports
import sys

# define a function that checks to see if the system is a linux platofrm
#
def linux_checker ():
    if "linux" not in sys.platform:
        raise RuntimeError ("Function can only run on Linux systems")
    else:
        print ("Do linux tasks")

print ("Is this a Linux system")

try:
    linux_checker ()
except:
   print ("Linux function wasn't executed")

print ("End of program")