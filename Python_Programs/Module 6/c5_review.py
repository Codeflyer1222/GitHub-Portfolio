#!/bin/bash
#
#!/usr/bin/env python3
#
# Problem: Chapter 5 review examples
# Author: instructor
# Date: 16 Feb 26
#
# create a list of class titles
myclasses = ['CIST1601', 'CIST2431', 'CIST2451', 'CIST2742']
required_courses = ['CIST1601', 'CIST2431', 'CIST2451', 'CIST2742', 'CIST1122']

# check to see if CIST1601 and CIST 2432 are members of the classes list
'CIST1601' in myclasses
'CIST2432' in myclasses


# conditional to see if CIST2432 not a member of the classes list
myclass = 'CIST2432'
if myclass not in myclasses:
    print (f"{myclass} is not a member of the list myclasses")
else:
    print (f"{myclass} is a member of the list myclasses")


#myclass = 'CIST2431'
#myclass = 'CIST1122'
myclass = 'ENGL1102'
if myclass in myclasses:
    print (f"Student registered for {myclass}")
elif myclass in required_courses:
    print (f"Student is not registered for the required course {myclass}")
else:
    print (f"{myclass} is not a required course")

#ORDER OF PRECEDENCE FOR not and or. 