#!/usr/bin/env python3
#
# Problem: Chapter 8 class Examples
# Files:
#     <files required by this file>
# 
# Author: instructor
# Date: 25 jun 2025
#
# Note - docstrings are written with "#" to make classroom demonstration easier
#

#DEFINE CONSTANTS THEN FUNCTIONS
# no arguments
#DEFINE FUNCTIONS FIRST BEFORE YOU CALL THEM
def greeting ():
    #DONT PUT DOUBLE QUOTES IN FUNCTION B/C READ AS CODE
    # Display a simple greeting 
    print ("Hello from greeting function")

greeting ()

#
# one parameter
def greeting2 (fname):
    # Display a simple greeting with parameter/arguement
    print (f"2. Hello {fname} from greeting function")
    sum = 0

greeting2 ("students")
myname = "instructor"
greeting2 (myname)
myname = "CIST2742"
greeting2 (myname)

#
# show error message
#PARAMETER IS VALUE IN THE PARENTESES WHEN DEFINING. CALLING IS CALLED ARGUMENTS
def greeting3 (fname, lname):
    # Display a simple greeting with error due to not enough arguments 
    print (f"3. Hello {fname} {lname} from greeting function")

greeting3 ("students")

#
# positional arguments
#WHEN YOU CALL FUNCTION, USE TWO ARGUMENTS
def greeting4 (fname, lname):
    # Display a simple greeting with positional agruments
    print (f"4. Hello {fname} {lname} from greeting function")
    fname = "Sarah Sue"
    print ("fname in greeting4", fname)


# call greeting4 with various arguments
greeting4 ("CIST","Student")
myname = "instructor"
yourname = "student"
#SCOPE OF VARIABLE IS DIFFERENT FROM FUNCTION VARIABLES/ARGUMENTS CALL
greeting4 (myname, yourname)

fname = "instructor1"
lname = "student1"
greeting4 (fname, lname)
print ("fname after call to greeting4", fname)

firstn = "Winnie"
lastn = "Pooh"

#THE VALUE OF ARGUMENTS IS RELATIVE TO POSITION
greeting4 (firstn, lastn)
greeting4 (lastn, firstn)

# greeting5 function deleted; not needed simply call greeting4 multiple times

# keyword arguments
def greeting6 (fname, lname):
    # Display a simple greeting with keyword agruments
    print (f"6. Hello {fname} {lname} from greeting function")

#ASSIGNMENTS IS THE EQUAL SIGN. ARGUMENTS ARE NOT BASED ON POSITION ANYMORE.
#KEYWORD NAME AND VALUE. FREES YOU FROM USING ORDER
greeting6 (fname = "CIST", lname = "students")
greeting6 (lname = "students", fname = "CIST")
myname = "Tigger"
mylname = "TiggerToo"
greeting6 (lname = mylname, fname = myname)


#
#default values
def greeting7 (lname, fname = ""):
    # Display a simple greeting with default value agruments
    if fname != "":
        print (f"7. Hello {fname} {lname} from greeting function")
    else:
        print ("No fname given")

greeting7 ("students")
greeting7 ("students", "CIST")
greeting7 (fname = "CIST", lname = "students")
#greeting7 (fname = "CIST", "students")   # causes an error
greeting7 ("students", fname = "CIST", ) 

#
studentNo = 34
def greeting8 (lname, studentNo, fname = ""):
    # Display a simple greeting with default value agruments and none default values
    print (f"8. {fname} {lname} student's number is {studentNo}")

greeting8 ("students", studentNo)
studentNo = 17
greeting8 ("students", studentNo, fname = "CIST")
greeting8 (studentNo = 51, fname = "CIST", lname="students")
greeting8 ( fname = "CIST", lname="students", studentNo = 68)

#
# calcualte the sum of 2 numbers

def myadd (num1, num2):
    # Calculate a value and return it to calling function
    sum = num1 + num2

    print (f"The sum of {num1} and {num2} : {sum:14.0f}")
    #print ("The sum variable is located at address: ", id (sum))
    return (sum)

addend1 = 5
addend2 = 7
#sum_returned = myadd (addend1, addend2)
sum_returned = myadd (addend1, addend2)
print (f" The sum is {sum_returned}, {type (sum_returned)}")
#print ("sum returned is located at address", id (sum))

sum_returned = myadd (35, addend2)
print (f" The sum is {sum_returned}, {type (sum_returned)}")

sum_returned = myadd (addend1, 198.5)
print (f" The sum is {sum_returned}", {type (sum_returned)})

sum_returned = myadd (45.4, 50.2)
print (f" The sum is {sum_returned}", {type (sum_returned)})

#
# returning a dictionary

def student_list (fname, lname, studentno, class_no):
    # Build a dictionary of student information
    studentinfo = {'first':fname, 'last':lname, 'snum':studentno, 'cnum':class_no}
    return (studentinfo)

fname = 'Winnie'
lname = 'Pooh'
studentno = 76
class_no = '2431'
class_role = student_list (fname, lname, studentno, class_no)
print ("The student dictionary created ", class_role)

# Call the student info directiory builder function multiple times to build a class roster
fname = 'Winnie'
lname = 'Pooh'
studentno = 1
class_no = '2431'
class_role2 = student_list (fname, lname, studentno, class_no)
print (f"The class role contains 1 student {class_role2}")

fname = 'Tigger'
lname = 'Too'
studentno = 2
class_no = '2431'
class_role2 = student_list (fname, lname, studentno, class_no)

#the 2nd call to student_list replaces the value in class_role2
print (f"The class role contains 2 students {class_role2}, {type (class_role2)}")         # actually it only contains one!

# Call the student info directiory builder function multiple times to build a class roster 
#     Adding the student to the roster
classlist_roster = {}

fname = 'Winnie'
lname = 'Pooh'
studentno = 76
class_no = '2431'
# use the student no. as the key
class_role3 = student_list (fname, lname, studentno, class_no)
classlist_roster [studentno] = class_role3

fname = 'Tigger'
lname = 'Too'
studentno = 54
class_no = '2431'
class_role3 = student_list (fname, lname, studentno, class_no)
classlist_roster [studentno] = class_role3

print (f"The class roster is ")
for student in classlist_roster:
    print (f"{classlist_roster [student]}")
    
print ("The class_role3 variable is of type ", type (class_role3), " and the classlist_roster is of type ", type (classlist_roster))

print ("The class roster variable printed", classlist_roster)

#calling a function from within a while loop

classlist_roster = {}

cont_processing = "yes"
while cont_processing.lower () == "yes":
    # get student data from user
    fname, lname, student_no, class_no = input ("Enter the first name, last name, student number and class number for student (separated by a comma): ").split (",")
    
    # build student list dictionary and add to classlist roster
    class_role4 = student_list (fname, lname, student_no, class_no)
    classlist_roster [student_no] = class_role4
    for student in classlist_roster:
        print (f"The class role {classlist_roster[student]}")

    # determine whether user wants to continue
    cont_processing = input ("Do you want to continue? (Enter yes or no)")
    print (classlist_roster)
    
print ("Good Bye")

# modifying a list within a function

def add_a_fruit (fruit_list, fruit):
    # Add the given fruit to the list
    fruit_list.append (fruit)

    # print the list
    print (f"The list of fruits after adding {fruit}")
    print_list (fruit_list)

def print_list (list_2_print):
    # Print the list passed to the function
    print ("The list of fruits")
    for item in list_2_print:
        print (item)
    sum = 5
    print ("sum in print_list: ", sum, id(sum))

sum = 10
fruits = ["apple", "pears", "cherry", "dragonfruit"]
print ("The initial list of fruits: ")

#FUNCTION DOES NOT CHANGE VARIABLE
add_a_fruit (fruits, "watermelon")

#FUNCTION GETS CHANGED BY APPEND STATEMENT
add_a_fruit (fruits, "peach")
print ("sum in top level code: ", sum, id(sum))

# preventing a function from modiyfing a list

def modify_list_without_changing (mytemplist):
    # this function modifies a copy of the list and returns
    
    mytemplist.append (2742)
    mytemplist[0] = 2431
    return (mytemplist)

# define list
mylist = [1,2,3]

# print original list and call the function to change
# this execution will not change as the list is sent
print ("My 2nd original list", mylist)
mynewlist = modify_list_without_changing (mylist)
print ("My 2nd original list", mylist)
print ("My changed 2nd list", mynewlist)

# redefine list
mylist2 = [1,2,3]

# # print original list and call the function to change
# this execution will change as a reference to the list is sent
print ("My original list", mylist2)
#[:] STOPS LIST FROM CHANGING
mynewlist2 = modify_list_without_changing (mylist2[:])
print ("My original list", mylist2)
print ("My changed list", mynewlist2)

#
# passing an arbitary number of arguments
# sum the list of numbers

#*argv IS A VECTOR
#ARGUMENT ONE IS COMMAND. THE REST ARE ARGUMENTS. THIS IS HOW LINUX COMMANDS WORK
def myarg_list (arg1, *argv):
    # Variable number of arguments example
    # arg1 = 1st argument
    # argv = is a tuple containing the rest of the arguments
    print ("Argument 1 = ", arg1)
    for item in argv:
        print ("Argument *argv : ", item)

myarg_list ('Hello', 'Class', 'this', 'is', 'my', 'message')
myarg_list ("Good-bye")
myarg_list ()   # This statement will cause an error as at least one argument is required (arg1)

def sum_list (*args):
    # Sum the parameters sent
    return sum (args)

print (sum_list (1, 2, 3, 4, 5))
print (sum_list (5, 10, 15))
print (sum_list ())

#**kwargs IS AN ARBITARY NUMBER OF ARGUMETNS AND U DONT KNOW WHAT KIND
#BECOMES KEY VALUE PAIRS
#NOT NECESSARY FOR THIS WEEK'S ASSIGNMENT
def sum_list2 (**kwargs):
    # sum a list of variables
    sum =  0
    for k, val in kwargs.items ():
        print (k, val)
        sum = sum + val
    return (sum)

total = sum_list2 (a=1, b=2, c=3)
print ("The total of sum_list2 is ", total)


def student_list2 (fname, lname, **student_info):
    # Build a dictionary of known student information
    student_info ['first_name']= fname
    student_info ['last_name'] = lname
    return student_info

student_profile = student_list2 ("Winnie", "Pooh",
                                 student_no = 1, 
                                 class_no = "CIST2431")
print (f"The student_profile contains: {student_profile}")