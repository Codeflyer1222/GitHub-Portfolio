#!/usr/bin/env python3
#
# Problem: Rock, Paper, or Scissors
# Files:
# N/A
#
# Author: Samuel Brown
# Date: 14 FEB 2026
#
# provide comments for each section of code

#Title of program
print("First, Second, or Both")

#The first and second whole number entered by the user
FirstNmbr = int(input("\nEnter first number: "))
SecondNmbr = int(input("Enter second number: "))

#for loop that adds 1 to the iterative, index, through each loop starting at 1 until it reaches 100
for index in range(1, 101):
    #formula to calculate a factor of the multiple of FirstNmbr and SecondNmbr
    Scissors = index / SecondNmbr
    #asks if both values are the same factor for the multiple of both variables described in the formula
    if Scissors == FirstNmbr:
        #prints to screen the multiple of FirstNmbr and SecondNmbr
        print(index, " --> Scissors")
    #asks if the iterative is a multiple of the FirstNmbr
    elif index % FirstNmbr == 0:
        #prints the multiple of the FirstNmbr
        print(index, "--> Rock")
    #asks if the iterative is a multiple of the SecondNmbr
    elif index % SecondNmbr == 0:
        #prints the multiple of the SecondNmbr
        print(index, "--> Paper")