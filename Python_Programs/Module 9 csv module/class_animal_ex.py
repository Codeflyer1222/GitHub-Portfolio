#!/usr/bin/env python3
#
# Problem:class example of class definition
# Files:
#     class_animal_ex.py
# 
# Author: instructor
# Date: 21 Jun 2025
#

class Animal:
    """ A model of a Animal"""
    #IS THIS INSTANTIATION? KNOW ATTRIBUTES, METHODS, AND INSTATIATES.
    #THIS IS A METHOD.
    #self IS THE OBJECT PASSED TO THE CLASS
    def __init__ (self, age, gender):
        """ Initialized name and age attributes """
        self.age = age
        self.gender = gender
        self.mammal = False
      

    def isMammal (self):
        """ Simulate a duck swimming """
        print (f"is mammal. {self.mammal}")
    
    def mate (self):
        """Does the animal have a mate """
        print (f"The anminal has a mate")


#WE ARE INSTATIATING THE OBJECT (VARIABLE) OF A CLASS.
myAnimal = Animal (102, "Male")
myAnimal2 = Animal (110, "Female")

print (f"Animal's age is {myAnimal.age}")
print (f"Animal gender {myAnimal.gender}")
print (f"Animal mammal {myAnimal.mammal}")
print (f"Animal's weight is {myAnimal.weightlbs}")

myAnimal.weight (150)
print (f"Animal's weight is {myAnimal.weightlbs}")

myAnimal.isMammal ()
myAnimal.mate ()

myAnimal.mammal = True
print (f"Animal mammal {myAnimal.mammal}")

#USE DOT NOTATION JUST LIKE IN MODULES TO GET ACTUAL VALUE. JUST THE OBJECT SHOWS THE DATA LOCATION
print(myAnimal)