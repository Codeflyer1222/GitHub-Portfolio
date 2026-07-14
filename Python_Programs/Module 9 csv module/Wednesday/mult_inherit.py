#!/usr/bin/env python3
#
# Problem: Example of multiple inheritance
# Files:
#     
# 
# Author: instructor
# Date: 21-jun-25
#
# define Person class
class Person:
    def __init__(self, name):
        self.name = name

# define Job class
class Job:
    def __init__(self, salary):
        self.salary = salary

# define Employee class
class Employee(Person, Job):  # Inherits from both Person and Job
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)

    def details(self):
        print(self.name, "earns", self.salary)

# create an instance of an Employee
emp = Employee("Pooh", 50000)
emp.details()