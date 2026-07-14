#!/usr/bin/env python3
#
# Problem: CSV FILE utilization >
# Files:
#     <files required by this file>
# 
# Author: 
# Date: 12 March 2025
#
# This file shall be utilized during lecture to learn about manipulzting 
# csv files in python.

import csv

# a file in the current directory
FILENAME = "newtrips.csv"

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def read_mpg ():
    data = []
    with open (FILENAME) as file:
        reader = csv.reader (file)
        for row in reader:
            data.append (row)
    return data

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    trips = []
    trips = read_mpg()
    print ("The initial set of data is ", trips)
    
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
            
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        trip = [miles_driven, gallons_used, mpg]
        trips.append(trip)
                
        more = input("More entries? (y or n): ")

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips) 
    
    print("Bye!")

    print ("The updated data is ", trips)
    
if __name__ == "__main__":
    main()

