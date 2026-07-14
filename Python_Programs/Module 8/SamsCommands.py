#!/usr/bin/env python3
# Problem: Contact Manager 8-3
#
# Files: N/A
#
# Author: Samuel Brown
# Date: 4 March 2026

#defining the list command requiring the list in other program as argument.
#Each contact is listed in numerical order
def list(ContactList):
    #iterating through each name in each list
    for EachList in range(len(ContactList)):
        #printing the first item in each list, the name, defined in other program
        print(f"{EachList + 1}. {ContactList[EachList][0]}")

#Defining view command. First parameter is first list, Second paramter is the 2nd list/Contact Information
#of specified person by number
def view(ContactList):
    #Asking for which contact by number
    SpecifiedList = int(input("Number: "))

    #Error Checking
    if SpecifiedList <= 0 or SpecifiedList > len(ContactList):
        print("The number is not in the list of contacts. Try again")
    else:
        #print all info of specified list and seperate each value in list with new line
        print(f"Name: {ContactList[SpecifiedList - 1][0]}\nEmail: {ContactList[SpecifiedList - 1][1]}\nPhone: {ContactList[SpecifiedList - 1][2]}")

#defining add command
def add(ContactList):
    #append number to first layer of list, then string input of the values for the 2nd layer of list
    #WHY ISNT APPEND WORKING? 
    TheNewName = input("Name: ")
    Email = input("Email: ")
    Phone = input("Phone: ")
    NewContact = [TheNewName, Email, Phone]
    ContactList.append(NewContact)

   # ContactList.append(f"Name: {TheNewName}\nEmail: {Email}\nPhone: {Phone}")
    print(f"{TheNewName} was added.")

#Defining the del command to remove a list
def delete(ContactList):
    #Asking user for which contact to delete
    SpecifiedList = int(input("Number: ")) - 1

    #Error Checking
    if SpecifiedList + 1 <= 0 or SpecifiedList + 1 > len(ContactList):
        print("The number is not in the list of contacts. Try again")
    else:
        #Notifying user the contact is deleted
        print(f"{ContactList[SpecifiedList][0]} was deleted.")
        #Deleting the Contact
        del(ContactList[SpecifiedList])