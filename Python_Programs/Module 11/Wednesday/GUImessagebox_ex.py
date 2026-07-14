#!/usr/bin/env python3
#
# Problem: <tkinter root window demonstration>
# Author: instructor
# Date: 2025
#
# basic pop up window with message
#
import tkinter as tk
from tkinter import messagebox
#
# initialize label constant
LABEL_MESSAGE = " This program displays the operation of messagebox pop-ups. \nIn this window the user would be interfacing with the program."

# Build root window
root = tk.Tk ()
root.title ("MessageBox Practice")
root.geometry ("500x400")


root_label = tk.Label (root, text = LABEL_MESSAGE, font = "50")
root_label.pack ()

# create information pop-up
messagebox.showinfo ("Info", "This is an infomration pop up")
#
# create a warning pop up
messagebox.showwarning ("Warning", "This is a warning pop up")
#
# create an error pop up
messagebox.showerror ("Error", "This is an error pop up")
#
# create ask yes or no
response = messagebox.askyesno ("Confirm closing", "Do you want to close the program?")
if response == True:
    print ("Close program")
else:
    print ("Do not close the program")
#
# create a Ok or cancel
response1 = messagebox.askokcancel ("Confirm closing", "Do you want to close the program?")
if response1 == True:
    print ("Cancel program")
else:
    print ("Do not cancel the program")

root.mainloop ()