#!/usr/bin/env python3
#
# Problem: Chatper 6 examples
# Files:
#     student_ex.py
# 
# Author: instructor
# Date: 21 Feb 2025
#
# simple examples of directory creation and deleting items
#
# create a directory; show how to display items
#NO DUPLICATE KEYS IN A DICTIONARY. A KEY WILL OVERWRITE ANOTHER KEY.
message = {1:"Hello", 
           2: "World",
           3: 137
          }

print (message)
print (message [1])
#THE GET METHOD REQUIRES A PARAMETER THAT IDENTIFIES THE KEY TO RETRIEVE
print (message.get (2))
print ()
print ("Is there a blank line?")
print ()


# print 5th letter of key = 2 element
#[4] GETS THE LETTER d. ONLY WORKS FOR STRINGS
print (message[2][4])

# Test 2nd index on non string element
#print (message [3][2])   #<== causes an error. OBJECT IS NOT SUBSCRIPTABLE. FORESHADOWING?
print (message [3])



alien_0 = {"color": "green", "points": 5}
print (alien_0)
print (alien_0 ["color"])
print (alien_0.get ("points"))

# can set a return value is no key exists
get_item = alien_0.get ("type", "No such key")
print ("Value returned from get when key does not exist ", get_item)



# adding a new key and value. KEY ASSIGNMENT
message [4] = "Good-bye to be in CIST 2742"
print (message)

message ['four'] = "This value's key is 'four'"
print (message)

message [100] = 1000
print (message)

# delete an item from the dictionary
del message [2]
print (message)

# the following statements demonstrate the assignment of value
print (message)
message [4] = "Good-bye to be in CIST 2742"
print (message)

message [4] = "This is a changed value"
print (message)

message [1] = 2742
print (message)

message [2] = "Hello World"
print (message)



# using pop method with dictionaries
print (message)
#REQUIRES ARGUMENT FOR DICTIONARY. NOT FOR LIST?
#delitem = message.pop ()  #this causes an error
#print (delitem)
#delitem = message.pop ('color') #this causes an error
#print (delitem)
#POP 
delitem = message.pop (4, "UNKONWN")
print (delitem)
delitem = message.pop (3, "UNKNOWN")
print (delitem)

# using del function with dictionaries
del message[1]
print (message)



print ("Current message dictionary ", message)
print ("loop through a dictionary")
# looping through a dictionary
#for dkey, ditem in message:   #<== this causes an error
#.items GRABS THE WHOLE KEY VALUE PAIR
for dkey, ditem in message.items():
    print (dkey, ditem)

# loop through by key
#.keys JUST GRABS THE KEY
for dkey in message.keys():
    print (f"Key: {dkey}")



phonebook = {'winnie': '1234567890',
             'tigger': '4567890123',
             'adam': '7890123456',
             'rho': '1350982648'
             }
print (phonebook)
# sort the dictionary
#sort changes the memory. sorted DOES NOT CHANGE THE MEMORY
for name in sorted (phonebook.keys()):
    print (f"Key: {name}")

# work with the values
for value in phonebook.values():
    print (f"value: {value}")

# add another entry that has the same value
phonebook ['kanga'] = '1350982648'
print ("Updated phonebook: ", phonebook)

for value in phonebook.values():
    print (f"value: {value}")

