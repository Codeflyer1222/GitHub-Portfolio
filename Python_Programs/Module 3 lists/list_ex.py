#!/usr/bin/env python3
#
# Problem: C3 List examples
# Files:
#     NA
# 
# Author: instructor
# Date: 27 May 2025
#
# provide comments for each section of code

emptylist = []

# creation with assignment
fruits = ["watermelon", "kiwi", "peach", "apple", "watermelon"]
print (fruits, type (fruits))
"""
scores = [98, 100, 50, 78, 95, 100, 50]
print (scores, type (scores))

mixed_list = [98, "strawberry", 50.7, "pear", 95]
print (mixed_list, type (mixed_list))

#creation with list () constructor
list_fruits2 = list (("apple", "bannana", "cherry", "strawberry"))
print (list_fruits2)

#indexing a list
#negative is working backwards. COLON IS ONE TO THE END, BUT STOPS AT 3. 1:3. BUT :2 STARTS AT BEGINNING AND ENDS AT 2. 
print (fruits [0], fruits [-1], fruits [1:3], fruits [:2], fruits [-2:])

#index not in range
#print (fruits [5])

"""
# Modify list with assignment
fruits [4] = 'strawberry'
#CHANGING VALUE OF INDEX ITEM
fruits [-1] = "banana"

# add to the END of the list - append
fruits.append ("orange")
fruits.append (95)

#add to the MIDDLE of the list
fruits.insert (4, "watermelon")

fruits.insert (2, "grape")

print (fruits)

#deleting an item from the list
fruits.remove (95)
print (fruits)
#ONLY REMOVES THE FIRST ONE
fruits.remove ("watermelon")
print (fruits)

# pop the item off. WILL POP LAST ONE WITHOUT A VALUE. ALSO GIVE THE popped_fruit VARIABLE THE VALUE OF WHATS POPPED.
popped_fruit = fruits.pop (2)

print (fruits, "\n", popped_fruit, "\n")

#remove with del
del fruits[4]
print (fruits)
print (popped_fruit)

# sort the list
fruits2 = fruits
print (fruits)
fruits.sort()
print (fruits)
fruits.sort(reverse=True)
print (fruits)

# sort list but do not change the order
print ()
print (fruits2)
print (sorted (fruits2))
print (fruits2)
print (fruits2.reverse())

print (fruits2)

# determine how many items are in the list
lenOffruits = len (fruits2)
print (lenOffruits)
