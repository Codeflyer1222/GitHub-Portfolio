#!/usr/bin/env python3
#
# Problem: CSV FILE utilization >
# Files:
#     <files required by this file>
# 
# Author: 
# Date: 12 March 2025
#
# This file shall be utilized during lecture to learn about reading
# csv files in python.

import csv

# a file in the current directory
FILENAME = "customers.csv"

def read_mpg ():
    data = []
    with open (FILENAME) as file:
        stuff_in_file = csv.reader (file)
        for row in stuff_in_file:
            print (row)
            data.append (row)
    return data

def main():
    # display a welcome message
    print("Reading the mpg file")
    print()

    # read data file
    trips = read_mpg ()

    # print data in file
    print ("\n This is the data returned")
    print (trips)
    
    print("Bye!")

if __name__ == "__main__":
    main()

