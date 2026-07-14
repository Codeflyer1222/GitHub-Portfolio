#!/usr/bin/env python3
# Problem: Contact Manager 8-3
#
# Files: N/A
#
# Author: Samuel Brown
# Date: 4 March 2026

#import my premade functions from other file
import SamsCommands
#Title
print("Contact Manager\n")

#2 dimensional list of contacts
#CAN I HAVE MULTIPLE VALUES ASSIGNED TO ONE KEY?
Contacts = [["Guido van Rossum","FIRST@email.org","123-456-0789"],
            ["Eric Idle", "SECOND@email.org", "098-765-4321"]]

PARAMETER = True

while PARAMETER:
    #List of commands for user
    print(f"COMMAND MENU\n\
list - Display all contacts\n\
view - View a contact\n\
add - Add a contact\n\
del - Delete a contact\n\
exit - Exit program\n")
    
    #User's command input
    Command = input("Command:\t")

    #execution of commands
    if Command == "list":
        SamsCommands.list(Contacts)
        print("\n")
    elif Command == "view":
        SamsCommands.view(Contacts)
        print("\n")
    elif Command == "add":
        SamsCommands.add(Contacts)
        print("\n")
    elif Command == "del":
        SamsCommands.delete(Contacts)
        print("\n")
    elif Command == "exit":
        print("Bye!")
        PARAMETER = False
    else:
        print("Incorrect command. Try again")