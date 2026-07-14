#!/usr/bin/env python3
#
#!/usr/bin/env python3
#
# Problem: Number Converter Project 6-1
# Author: Samuel Brown
# Date: 22 Feb 26

#Title
print("Number Generator\n")

#number input by the user
Number = input("Enter a number: ")

#the number segmented into a list of digits
NumberList = list(Number)

#dictionary of word equivalent numbers when referencing the single's, hundred's, or thousand's place
ListOfOnes = {
    "0":"",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}

#dictionary of word equivalent numbers when referencing the ten's place or teen numbers
ListOfTens = {
    "0":"",
    "1":"ten",
    "2":"twenty",
    "3":"thirty",
    "4":"forty",
    "5":"fifty",
    "6":"sixty",
    "7":"seventy",
    "8":"eighty",
    "9":"ninety",
    "11":"eleven",
    "12":"twelve",
    "13":"thirteen",
    "14":"fourteen",
    "15":"fifteen",
    "16":"sixteen",
    "17":"seventeen",
    "18":"eighteen",
    "19":"nineteen"
}

#Checking to see if the User's number is negative
if "-" in Number:
    #Negative ones place
    if len(NumberList) == 2:
        print(f"{Number} is negative {ListOfOnes[NumberList[-1]]}")
    #Negative tens place
    elif len(NumberList) == 3:
        if "0" in Number:
            print(f"{Number} is negative {ListOfTens[NumberList[-2]]}")
        elif int(Number) > -20 and int(Number) < -10:
            print(f"{Number} is negative {ListOfTens[Number[1:]]}")
        else:
            print(f"{Number} is negative {ListOfTens[NumberList[-2]]}-{ListOfOnes[NumberList[-1]]}")
    #Negative hundreds place
    elif len(NumberList) == 4:
        #if ones place is zero, like 120
        if NumberList[-1] == "0":
             print(f"{Number} is negative {ListOfOnes[NumberList[-3]]} hundred {ListOfTens[NumberList[-2]]}")
        #if tens place is zero, like 102
        elif NumberList[-2] == "0":
            print(f"{Number} is negative {ListOfOnes[NumberList[-3]]} hundred and {ListOfOnes[NumberList[-1]]}")
        #if all three places have a number greater than 0, like 123
        else:
            print(f"{Number} is negative {ListOfOnes[NumberList[-3]]} hundred {ListOfTens[NumberList[-2]]}-{ListOfOnes[NumberList[-1]]}")
    
    #Negative thousands place
    #Created a for loop that iterates through each character of the User's input and then appends the dictionary word
    #eqiuvalent to a string.
    elif len(NumberList) == 5:
        #compare each part of the user's input to the dictionary, and then append the corresponding
        #value to the variable ConvertedNumber so I can just print the user's number and the variable.
        #Below is string output of word equivalent of user input number
        ConvertedNumber = ""
        #iterating through each digit of the Number input by the user. Uses negative number to read from right to left.
        for i in range(-4, 0, 1):
            #Adding the tens place word equivalent to the output
            if i == -2 and int(NumberList[-2]) > 0:
                ConvertedNumber += ListOfTens.get(NumberList[i])
                #Adding the ones place word equivalent to the output
                if int(NumberList[-1]) > 0:
                    ConvertedNumber += "-"
            else:
                #Adding the hundreds place word equivalent to the output
                ConvertedNumber += ListOfOnes.get(NumberList[i])
                if i == -3 and int(NumberList[-3]) > 0:
                    ConvertedNumber += " hundred "
                #Adding the thousands place word equivalent to the output
                elif i == -4 and int(NumberList[-4]) > 0:
                    ConvertedNumber += " thousand "
        print(f"{Number} is negative {ConvertedNumber}")
       
#If the User's number is positive then:
#Positive ones place
elif len(NumberList) == 1:
    #If the User just inputs 0 then it spits out zero
    if Number == "0":
        print("0 is zero")
    #printing a single digits word equivalent based on the dictionary
    else:
        print(f"{Number} is {ListOfOnes[NumberList[0]]}")

#Positive tens place
elif len(NumberList) == 2:
    #If there is no number in the ones place, then just print the number from the dictionary
    if "0" in Number:
        print(f"{Number} is {ListOfTens[NumberList[0]]}")
    #If the User's input Number is a teen number, like above 10 but below 20, then print that from the dictionary
    elif int(Number) > 10 and int(Number) < 20:
        print(f"{Number} is {ListOfTens[Number]}")
    #print the word equivalent of the User's number from both dictionaries
    else:
        print(f"{Number} is {ListOfTens[NumberList[0]]}-{ListOfOnes[NumberList[1]]}")

#Positive hundreds place
elif len(NumberList) == 3:
    #if ones place is zero, like 120
    if NumberList[-1] == "0":
        print(f"{Number} is {ListOfOnes[NumberList[-3]]} hundred {ListOfTens[NumberList[-2]]}")
    #if tens place is zero, like 102
    elif NumberList[-2] == "0":
        print(f"{Number} is {ListOfOnes[NumberList[-3]]} hundred and {ListOfOnes[NumberList[-1]]}")
    #if all three places have a number greater than 0, like 123
    else:
        print(f"{Number} is {ListOfOnes[NumberList[-3]]} hundred {ListOfTens[NumberList[-2]]}-{ListOfOnes[NumberList[-1]]}")

#Thousands place
#Created a for loop that iterates through each character of the User's input and then appends the dictionary word
#eqiuvalent to a string.
elif len(NumberList) == 4:
    #compare each part of the user's input to the dictionary, and then append the corresponding
    #value to the variable ConvertedNumber so I can just print the user's number and the variable.
    #Below is string output of word equivalent of user input number
    ConvertedNumber = ""
    #iterating through each digit of the Number input by the user. Uses negative number to read from right to left.
    for i in range(-4, 0, 1):
            #Adding the tens place word equivalent to the output
            if i == -2 and int(NumberList[-2]) > 0:
                ConvertedNumber += ListOfTens.get(NumberList[i])
                #Adding the ones place word equivalent to the output
                if int(NumberList[-1]) > 0:
                    ConvertedNumber += "-"
            else:
                #Adding the hundreds place word equivalent to the output
                ConvertedNumber += ListOfOnes.get(NumberList[i])
                if i == -3 and int(NumberList[-3]) > 0:
                    ConvertedNumber += " hundred "
                #Adding the thousands place word equivalent to the output
                elif i == -4 and int(NumberList[-4]) > 0:
                    ConvertedNumber += " thousand "
    #Final output displayed to screen
    print(f"{Number} is {ConvertedNumber}")
#If the user's input is a number too large or not even a number, then you get this "error"
else:
    print("outside of range")