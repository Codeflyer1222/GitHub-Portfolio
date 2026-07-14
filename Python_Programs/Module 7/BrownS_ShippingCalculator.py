#!/usr/bin/env python3
# Problem: Shipping Calculator Project 7-1
#
# Files: N/A
#
# Author: Samuel Brown
# Date: 26 Feb 26

#Title
print(f"==================================================================================================\n\
Shipping Calculator")

#While loop boolean condition
CONDITION = True

#While loop
while CONDITION:
    print("==================================================================================================")
    #Asking the user for cost of item
    ItemsCost = float(input("Cost of items ordered: "))
    #Rounding the user's number to 2 decimal points
    Rounded = round(ItemsCost, 2)
    #Error handling
    if Rounded < 0:
        print("You must enter a positive number. Please try again.")
        continue
    #Calculating shipping cost
    elif Rounded < 30.00:
        ShippingCost = 5.95
        print(f"Shipping cost:         {ShippingCost}")
    elif Rounded > 29.99 and Rounded < 50.00:
        ShippingCost = 7.95
        print(f"Shipping cost:         {ShippingCost}")
    elif Rounded > 49.99 and Rounded < 75.00:
        ShippingCost = 9.95
        print(f"Shipping cost:         {ShippingCost}")
    #Note: if I enter a number with at least 23 zeros (one hundred sextillion), the program will show
    #a slightly smaller number than entered because of a limitation on the amount of data stored in binary
    elif Rounded > 74.99:
        ShippingCost = 0
        print(f"Shipping cost:         FREE!")
    Total = Rounded + ShippingCost
    #Output of Total cost
    print(f"TotalCost:             {Total:.2f}")

    #Asking user to change the condition for closing or continuing the loop
    while CONDITION:
        Question = input("Continue?  (y/n):               ")
        if Question == "y":
            CONDITION = True
            break
        elif Question == "n":
            CONDITION = False
        #Error handling
        else:
            print("ERROR: only enter a 'y' or a 'n'")
            continue
#End of program
print("==================================================================================================\n\
Bye!")