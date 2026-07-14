#!/usr/bin/env python3
#
# Problem: Number Generator
# Files:
# N/A
#
# Author: Samuel Brown
# Date: 8 FEB 2026
#
# provide comments for each section of code

#Title
import random
print("Number Generator\n")

#The two inputs from the user
MinimumNmbr = int(input("Minimum number: "))
MaximumNmbr = int(input("Maximum number: "))

#Calculated List of numbers:
#The total
Total = MinimumNmbr + MaximumNmbr

#Generating random list of numbers within given range
count = 10
#The random function is turning my Numbers variable into a list, right???
Numbers = random.sample(range(MinimumNmbr, MaximumNmbr), count)
Numbers.sort()

#Output of all calculated numbers. Could've used min and max function but opted not to :)
print("\nTotal:\t", sum(Numbers), "\nAverage:\t", float(Total/2), "\nLargest:\t", Numbers[9], "\nSmallest:\t", Numbers[0], "\nNumbers: ", Numbers)