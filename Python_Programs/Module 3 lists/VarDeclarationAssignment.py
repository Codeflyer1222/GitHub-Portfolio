#!/bin/python3
#
# Following the directions provided, create an properly executed python program that displays the requested information.
# When complete, show the instructor the working code before leaving class.
# 
# Define 3 variables to prove that python is case sensitive by replacing the "{}". The only difference in your variables should be the case. 
# # Do not use myvar1, myvar2 or myvar3 as your variables.

print ("This code block shows how Python is case sensitive")

kiss = 1
Kiss = 2
KISS = 3

print ("VAR1 = ", KISS, "Var1 = ", Kiss, "var1 = ", kiss)

# Define variables as string, integer and float by replacing the "{}". The variable name should indicate the type of variable.
print ("This code block shows how Python can define strings, integers and floats")
PythonIsFun = "Python is fun "
Fifteen = " 15 "
OneHundoFive = " 105 "
FifteenValue = 15
FifteenValueDec = 15.0

# For each print statement, provide the appropriate variable name
print ("The alphabetic string: ", PythonIsFun, "\n The number string: ", Fifteen)
print ("One can not treat a number string as a number")
print ("However, one can 'perform' arithmetic operations on strings with other string", Fifteen + OneHundoFive)
print ("integerVar is an integer value: ", FifteenValue)
print ("floatVar is a decimal value", FifteenValueDec)
print ("Arithmetic operations can be preformed on variables representing numbers", FifteenValue + FifteenValueDec)

##### Before continuing show the instructor your working code

"""
After your working code has been graded by the instructor:

     1. Uncomment the following code block
     2. Determine what is incorrect about the code
     3. In the dropbox, for this assignment, provide a written response to the following -- What is the error? How would you correct the error?
"""


myvar1 = "22"
myvar2 = 21
myvar3 = myvar1 + myvar2
print ("myvar1 + myvar2 = ", myvar3)

