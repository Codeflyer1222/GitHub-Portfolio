#!/usr/bin/env python3
#
# Problem: Example of inheritance
# Files:
#     class_animal_ex.py - contains parent class definition
#     class_ex.py - this file
# 
# Author: instructor
# Date: 21-jun-25
#
# import the Animal class 

#GOES INTO FILE, PULLS THE MODULE FOR THIS CLASS TYPE
from class_animal_ex import Animal

# define the Duck class to be a child class of the existing class Animal
#DUCK INHERITS ANIMAL CLASS ATTRIBUTES
class Duck (Animal):
    """ A model of a Duck """
    def __init__ (self, name, age, gender):
        """ Initialized name and age attributes """
        #super() GIVES age and gender PARAMETERS VALUES FROM THE PARENT MODULE Animal
        super().__init__ (age, gender)
        self.name = name
        self.beakColor = "yellow"
        self.weight = 0

    def swim (self):
        """ Simulate a duck swimming """
        print (f"{self.name} is swimming.")
    
    def Quack (self):
        """Simulate a duck quacking"""
        print (f"{self.name} says Quack Quack")
    
    def update_duck_weight (self, weight):
        self.weight = weight

    def get_weight (self):
        print (f"{self.name} weights {self.weight} pounds")

    # over ride the mate method
    def mate (self):
        """Ducks do not have mates"""
        print (f"Ducks do not have mates")

myDuck = Duck ("Sam", 5, "male")
print (f"My duck's name is {myDuck.name}")
print (f"My duck's age is {myDuck.age}") # an inherited attribute
print (f"My duck's beak color is {myDuck.beakColor}")
print (f"{myDuck.name} is a {myDuck.gender}") # an inherited attribute
print (f"Is {myDuck.name} a mammal? {myDuck.mammal}") # this is an inherited method
myDuck.swim ()
myDuck.Quack ()

weight = (float (input (f"Enter {myDuck.name} weight: ")))
myDuck.update_duck_weight (weight)
print (f"Sam the duck weighs {myDuck.weight}")

myDuck.mate ()

myDuck2 = Duck ("Betty", 3, "female")
print (f"My duck's name is {myDuck2.name}")
print (f"My duck's age is {myDuck2.age}")
print (f"My duck's beak color is {myDuck2.beakColor}")
print (f"{myDuck2.name} is a {myDuck2.gender}")
myDuck2.swim ()
myDuck2.Quack ()
print (f"My duck weighs {myDuck2.weight}")
myDuck2.update_duck_weight (5)
myDuck2.get_weight ()
print (f"Sam the duck weighs {myDuck.weight}")
