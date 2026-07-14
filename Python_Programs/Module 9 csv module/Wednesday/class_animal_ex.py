#!/usr/bin/env python3
#
# Problem:class example of class definition
# Files:
#     class_animal_ex.py
# 
# Author: instructor
# Date: 21 Jun 2025
#
# define Animal Class
class Animal:
    """ A model of a Animal"""
    def __init__ (self, age, gender):
        """ Initialized name and age attributes """
        self.age = age
        self.gender = gender
        self.mammal = False
        self.weightlbs = 0

    def isMammal (self):
        """ Simulate a duck swimming """
        print (f"is mammal. {self.mammal}")
    
    def mate (self):
        """The animal has a mate """
        print (f"The anminal has a mate")

# instantiate 2 animal objects
# each object must have a unique name
myAnimal = Animal (102, "Male")
myAnimal2 = Animal (104, "Female")

# print myanimal's data
print (f"Animal's age is {myAnimal.age}")
print (f"Animal gender {myAnimal.gender}")
print (f"Animal mammal {myAnimal.mammal}")
print (f"Animal's weight is {myAnimal.weightlbs}")

# modify an attribute of the object (myAnimal)
myAnimal.weightlbs = 150
print (f"Animal's weight is {myAnimal.weightlbs}")

# call the object's methods
myAnimal.isMammal ()
myAnimal.mate ()

# modify an attribute of the object
myAnimal.mammal = True
print (f"Animal mammal {myAnimal.mammal}")
