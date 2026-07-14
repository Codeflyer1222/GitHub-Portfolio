#!/usr/bin/env python3
#
# Problem: Project 3-2: Tip Calculator
# Files:
# <files required by this file>
#
# Author: Samuel Brown
# Date: 2-FEB-2026

#introduction of program
print("Tip Calculator\n")

#prompt for user to enter cost of their meal
Meal = float(input("Cost of meal:\t"))

#15% subheader
print("\n15%")

#Forumula for a tip of 15 percent
FifteenTip = Meal * 0.15

#Output of a 15% tip amount and its total amount
print(f"Tip amount:\t {FifteenTip:.2f} \
       \nTotal amount:\t {Meal + FifteenTip:.2f}")

#20% subheader
print("\n20%")

#Formula for a tip of 20 percent
TwentyTip = Meal * 0.20

#Output of a 20% tip amount and its total amount
print(f"Tip amount:\t {TwentyTip:.2f} \
      \nTotal amount:\t {Meal + TwentyTip:.2f}")

#25% subheader
print("\n25%")

#Formula for a tip of 25 percent
TwentyFiveTip = Meal * 0.25

#Output of a 25% tip amount and its total amount
print(f"Tip amount:\t {TwentyFiveTip:.2f} \
      \nTotal amount:\t {Meal + TwentyFiveTip:.2f}")