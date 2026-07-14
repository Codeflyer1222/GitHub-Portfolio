#!/usr/bin/env python3
#
# Problem: Example of inheritance
# Files:
#     csv_writerow_vs_writerow_ex.py (this file)
#     creates: poohs_friends file
# 
# Author: instructor
# Date: 20 October -25
import csv

# file column header titles
fields_header = ['Name', 'Type', 'Year', 'GPA']

# data rows of csv file
data_2_write = [['Pooh', 'BEAR', '4', '4.0'],
        ['Tigger', 'TIGER', '2', '3.1'],
        ['Owl', 'BIRD', '2', '3.3'],
        ['Eeyore', 'DONKEY', '1', '3.5'],
        ['Rabbit', 'RABBIT', '3', '3.8'],
        ['Kanga', 'KANGAROO', '2', '3.1']]

# name of csv file
filename = "poohs_friends.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
#with open(filename, 'w', newline='') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields_header)

    # writing the data rows
    csvwriter.writerows(data_2_write)