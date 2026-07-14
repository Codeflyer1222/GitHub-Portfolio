#!/usr/bin/env python3
#
# Problem: Chatper 6 examples
# Files:
#     CIST2742_C6_ExamplesFiles.py
# 
# Author: instructor
# Date: 21 Feb 2025
#
num_list = []
#list FUNCTION MAKES EVERY CHARACTER A LIST
num_list = list (input ("Enter a list of nubmers: "))
print ("First print: ", num_list)
#THE .split METHOD SEPERATES CHARACTERS BY SPACES
num_list = list (input ("Enter a list of nubmers: ").split())
print ("Second print ", num_list)
#.split(",") USES , AS A DELIMITER. 
num_list = list (input ("Enter a list of nubmers: ").split(","))
print ("Third print ", num_list)