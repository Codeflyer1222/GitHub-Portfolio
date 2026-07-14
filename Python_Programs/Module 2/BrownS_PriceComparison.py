# Problem: Price Comparison
# Files:
# BrownS_PriceComparison.py
#
# Author: Samuel Brown
# Date: 22-JAN-2026
#
# provide comments for each section of code

#Prompt
print("Price Comparison\n\n")

#Price of first detergent input by user
detergent1 = float(input("Price of 64 oz size:\t"))

#Price of second detergent input by user
detergent2 = float(input("Price of 32 oz size:\t"))

#new line
print("")
#formula first item
PricePerOunce1 = detergent1/64


#formula second item
PricePerOunce2 = detergent1/32

#outcome rounded to two decimals
print(f"\nPrice per oz (64 oz):\t {PricePerOunce1:.2f}")
print(f"Price per oz (32 oz):\t {PricePerOunce2:.2f}")