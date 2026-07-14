#!/usr/bin/env python3
#
# Problem: Customer Class Unit Test
# Files: 
#
# Author: Samuel Brown
# Date: 3 April 2026

#Importing the CSV module to work with CSVs
import csv

#Title
print("Customer Viewer")

#Import modules
class Customer:
    """The __init__ method is always there. This gives the object the data of a customer to be used again
    in another method. It instantiates attributes of the class."""
    def __init__(self, cust_id, first_name, last_name, company, address, city, state, zip_code):
        self.id = int(cust_id)
        self.firstName = first_name
        self.lastName = last_name
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code




    """Displaying a customer's full address. The self parameter makes it an object method and uses data that has
    already been given to the object."""    
    def full_address(self):
        #contains the address in a list
        lines = []
        #Removes whitespace and checks for any data. If there is data, the condition is true and adds it to the list
        if self.company.strip():
            lines.append(self.company)

        lines.append(self.address)
        lines.append(f"{self.city}, {self.state} {self.zip}")
        #puts the data togther as one element
        return "\n".join(lines)

    def partial_address(self):
        #contains the address in a list
        lines = []
        #Removes whitespace and checks for any data. If there is data, the condition is true and adds it to the list

        lines.append(self.address)
        lines.append(f"{self.city}, {self.state} {self.zip}")
        #puts the data togther as one element
        return "\n".join(lines)