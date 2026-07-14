#!/usr/bin/env python3
# Problem: Customer Viewer 9-3
#
# Files: 
# Customers.csv
#
# Author: Samuel Brown
# Date: 9 March 2026

#Importing the CSV module to work with CSVs
import csv

#containing the CSV file in a variable
FILENAME = "customers.csv"
#Title
print("Customer Viewer")

class Customer:

    """The __init__ method is always there. This gives the object the data of a customer to be used again
    in another method."""
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

    """Turns the contents of the csv into a dictionary to make it more readable and easire to manipulate"""
    def load_customers(filename):
        customers = []
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                customers.append(Customer(
                    row["cust_id"],
                    row["first_name"],
                    row["last_name"],
                    row["company_name"],
                    row["address"],
                    row["city"],
                    row["state"],
                    row["zip"]
                ))
        return customers

    """Searches for the id input by the user"""
    def find_customer_by_id(customers, cust_id):
        #iterates through each customer
        for customer in customers:
            #If its the same one as requested then print
            if customer.id == cust_id:
                return customer
        return None


print("Customer Viewer\n")

customers = load_customers(FILENAME)

#Asking user to search for id in csv file or close program
PARAMETER = True

while PARAMETER:
    #Asking user for the requested ID. .strip() is for error handling
    user_input = input("Enter customer ID: ").strip()
    
    #more error handling
    if not user_input.isdigit():
        print("\nPlease enter a numeric ID.\n")
        continue
    
    #Turning the requested ID into an integer
    cust_id = int(user_input)
    print()

    customer = find_customer_by_id(customers, cust_id)

    if customer:
        print(customer.full_address)
        print()
    else:
        print("No customer with that ID.\n")

    again = input("Continue? (y/n): ").lower()
    print()
    if again != "y":
        PARAMETER = False

print("Bye!")
