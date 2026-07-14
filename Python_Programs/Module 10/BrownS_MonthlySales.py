#!/usr/bin/env python3
# Problem: Customer Viewer 9-3
#
# Files: 
# monthly_sales.txt
#
# Author: Samuel Brown
# Date: 29 March 2026

#import modules
from pathlib import Path

#Creating a file object
FILENAME = "monthly_sales.txt"


#Turn txt file into a csv file?

#The file as a dictionary
dictionary_file = {}

#Turn the txt file into a dictionary. Maybe turn it into a JSON file?
with open(FILENAME) as file:

    #Turning a line of text into a manipulative string
    for line_string in file:

        #Add the line to the dictionary
        dictionary_file[line_string[0:3]] = float(line_string[4:])

#Class for manipulating the txt file
class MonthlySales:
    #Using init to assign any arguments
    def __init__(self):
        #These are instance properties. They belong to each object.
        #self.whatevernameofobject = property
        #self is used to reference any other parameter or method.
        #to make object -> object = MonthlySales("property")
        #To use object -> print(object.property). The property part is optional
        #Method can use object property with self.property
        pass
    #The view command will ask user for month then display its key
    def view_txt_file(self):
        #Ask user for which month to search in the dictionary
        request_month = input("Three-letter Month: ")

        #search the global dictionary for the corresponding value
        print(f"Sales amount for {request_month} is {dictionary_file[request_month]}")

    #Function for totals command will sum all months' sales
    def totals_txt_file(self):

        #Adding the sum of all months
        total = sum(dictionary_file.values())

        #Printing the total
        print(f"Yearly total:\t{total}")

        #Finding the average
        average = total / len(dictionary_file)

        #Printing the average
        print(f"Monthly average:\t{average}")

    #The edited command will ask user for which month, then update the written changes to the key
    def edit_txt_file(self):
        #Ask user for which month to edit
        request_month = input("Three-letter Month: ")

        #Ask user for the new amount of sales for that month
        new_sales = input("Sales amount: ")

        #Make changes to the txt file
        #Ask for which month. Delete that line in the txt file. 
        #Then append a new line with the requested month, spacebar, and value
        with open(FILENAME, "r") as file:
            #Stores each line of the txt file as an item in a list
            all_the_lines = file.readlines()

            #This new list will be written in the updated txt file
            new_lines = []

            #Excluding the user's month, add all the same lines to the new list
            for single_line in all_the_lines:
                if single_line[0:3] != request_month:
                    new_lines.append(single_line)

        #Updating the file with the new list
        with open(FILENAME, "w") as file:
            #Rewriting the file with the made list
            file.writelines(new_lines)

        with open(FILENAME, "a") as f:
            f.write(f"{request_month} {new_sales}")
        
        #Remove the dictionary's contents and add the updated txt file
        dictionary_file.clear()

        #Update the dictionary
        with open(FILENAME) as file:

            #Turning a line of text into a manipulative string
            for line_string in file:

                #Add the line to the dictionary
                dictionary_file[line_string[0:3]] = float(line_string[4:])

def main():
    #Title of program  
    print(
    """Monthly Sales Program
    COMMAND MENU
    view    - View sales of a particular month
    edit    - Edit sales for specified month
    totals  - View sales summary for year
    exit    - Exit program
    """
    )

    #while loop until exited
    ACTIVE = True

    while ACTIVE:
        print()

        #Asking user for command
        user_command = input("\nCommand: ")

        #Making an object to execute any called command
        sales_app = MonthlySales()

        #exit command is entered
        if user_command == "exit":
            print("Bye!")
            ACTIVE = False
        
        #view command is entered
        elif user_command == "view":
            #Making an object executed the view_txt_file function
            sales_app.view_txt_file()

        #totals command is entered
        elif user_command == "totals":
            sales_app.totals_txt_file()

        #edit command is entered
        elif user_command == "edit":
            sales_app.edit_txt_file()

        #Incorrect user response
        else:
            print("Incorrect response. Try again\n")
        
main()

if __name__ == "__main__":
    main()