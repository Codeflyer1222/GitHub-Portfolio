#!/usr/bin/env python3
#
# Problem: Example of multilevel inheritance
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

# define Employee class
class Employee(Person):  
    def show_role(self):
        print(self.name, "is an employee")

#define Manager class
class Manager(Employee):  # Manager inherits from Employee
    def department(self, dept):
        print(self.name, "manages the ", dept, "department")

mgr = Manager("Tigger")
#mgr = Manager ()   # this causes a traceback
mgr.show_role()
mgr.department("mischief")