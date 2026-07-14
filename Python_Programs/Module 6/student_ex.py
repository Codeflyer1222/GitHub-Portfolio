#!/usr/bin/env python3
#
# Problem: Chatper 6 examples
# Files:
#     student_ex.py
# 
# Author: instructor
# Date: 21 Feb 2025
#
# use of the dict constructor. MAKES A DICTIONARY
class_instructor = dict ([("CIST2431", "winnie"), ("CIST2451", "Tigger"), ("CIST1601", "rho")])
#print (class_instructor)
 
# create a student nested directory
#
student = {
    '1001': {
        'first_name' : 'billy',
        'second_name' : 'bob',
        'course' : ['CIST2742', 'CIST2431'],
        'addr' : {
            'street': "Copse",
            'city': "Augusta",
            'zip_code': "30909",
            },
        },
    '1002': {
        'first_name' : 'sally',
        'second_name' : 'sue',
        'course' : ['CIST2742'],
    }
}
#print (student)

#3 DIMENSINOAL DICTIONARY
print(student ['1001']['addr']['city'])