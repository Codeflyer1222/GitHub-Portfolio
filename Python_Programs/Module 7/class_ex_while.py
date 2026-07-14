#!/usr/bin/env python3
#
# Problem:C7 while examples
# Files:
#     class_ex_while.py
# 
# Author: instructor
# Date: 25 Feb 25
#
# matrix defined
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
]

# a loop that counts to 5
for index in range (1,5):
    print (index)

print ("Now for the while loop")
index = 1
while index <  5:
    print (index)
    index += 1    # this is a must otherwise the loop goes forever

# flag - the following does not enter the while loop
# this implementation is confusing
stop = True
while stop:
    print ("Hello")
    stop = False
print ("while loop is finished 1")     

# flag - loop enters

stop = False
while not stop:
    print ("Hello 2nd loop")
    stop = True
print ("while loop is finished 2")  

# flag - loop enters
# clearer implementation

cont_processing = True
while cont_processing:
    print ("Hello 3rd loop")
    cont_processing = False
print ("while loop is finished 3")  

# allow user to determine when to quit
# requires user to enter a lower case string
prompt = "Type 'quit' to end data input for loop 4: "
cont_processing = ""
while cont_processing != "quit":
   print ("Hello")
   cont_processing = input (prompt)
print ("while loop is finished 4")  

# the previous implementation 
# requires user to enter a lower case string
# write code such that user can type quit in any form
prompt = "Type 'quit' to end data input for loop 5: "
cont_processing = ""
while cont_processing.lower () != "quit":
   print ("Hello")
   cont_processing = input (prompt)
print ("while loop is finished 5")  

# break
cont_processing = True
index = 1
while cont_processing:
    print ("Hello loop 6", index)
    index += 1
    if index == 3:
        break
print ("while loop is finished 6", index)

# break
index = 1
while index < 10:
    print ("Hello loop 7", index)
    index += 1
    if index == 6:
        break
print ("while loop is finished 7", index)  

# break isn't just for while loops
# print the values of matrix a row at a time
found = False
for row in matrix:
    print (f"row: ", end=":")
    #print (f"row: ")
    for item in row:
        print (f"{item} ", end=",")
        if item == 5:
            found = True
            break  # exits internal loop    ADD WHICH LOOP EACH BREAK IS BREAKING OUT OF.
    print ()
    if found:
        break  # exits exterior loop

print ("while loop is finished 8")     

#continue
index = 1
while index < 10:
    print ("Hello", index)
    index += 1
    #MULTIPLE OF 3?
    if index % 3 == 0:
         print ("Multiple of 3")
         #continue MAKES THE LOOP GO TO ITS NEXT ITERATION INSTEAD OF CLOSING THE LOOP WITH A break statement.
         continue
    print (f" loop repeating for index: {index}")
    
print ("while loop is finished 9")

# continue isn't just for while loops
# print the values 0 - 9 skipping 3 and 5
for index in range(0, 10):
    # If index = 3 or 5, then continue to the next iteration
    if (index == 3) or (index == 5):
        continue
    print(index)

print ("while loop is finished 10")     
# the following is an infinite loop - AVOID at all costs
index = 1
while True:
    print (x)
    x += 1
#CONTINUE AT WEDNESDAY'S CLASS
# issues with modifiying a list with a for statement
fruits = ["apple", "banana", "cherry", "dragonfruit"]
print (fruits)

for fruit in fruits:
    if fruit == "banana":
        fruits.remove("banana")
    print (fruit)
print (fruits)

# what happens when there are 2 bananas
fruits = ["apple", "banana", "banana", "cherry", "dragonfruit"]
print (fruits)

for fruit in fruits:
    if fruit == "banana":
        fruits.remove("banana")
    print (fruit)
print (fruits)

#  while does not work the same way
vegetables = ['peas', 'carrots', 'beans', 'broccoli']
while 'carrots' in vegetables:
    vegetables.remove ("carrots")
print  ("Updated vegetable list", vegetables)

vegetables = ['peas', 'carrots', 'carrots', 'beans', 'broccoli']
while 'carrots' in vegetables:
    vegetables.remove ("carrots")
print  ("Updated vegetable list", vegetables)

# moving items from one list to another
# add each user until there are no more new users
new_users = ['pooh', 'piglet', 'tigger']
processed_users = []
while new_users:
    user_to_process = new_users.pop()
    print (f"Adding user: {user_to_process.title ()}")
    processed_users.append (user_to_process)

print ("\nThe following users are added: ")
for processed_user in processed_users:
    print (processed_user.title ())

# remove duplicates
# for loops may not work correctly
# 2nd banana is not removed
fruits = ["apple", "banana", "banana", "cherry", "dragonfruit"]
print (fruits)
for fruit in fruits:
    if fruit == "banana":
        fruits.remove("banana")
    print (fruit)
print (fruits)

fruits = ["apple", "banana", "banana", "cherry", "dragonfruit"]
print ("Original fruit list", fruits)

#remove all instances of 'banana' from the list
while 'banana' in fruits:
    fruits.remove ('banana')
print ("Updated fruit list", fruits)

#reset fruits list with multiple apples
fruits = ["apple", "banana", "apple", "cherry", "apple", "dragonfruit"]
print ("Original fruit list", fruits)

#remove all instances of 'apple' from the list
while 'apple' in fruits:
    fruits.remove ('apple')
print ("Updated fruit list", fruits)
"""