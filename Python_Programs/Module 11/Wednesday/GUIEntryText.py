#!/usr/bin/env python3
#
# Problem: <tkinter entry retrival demonstration>
# Author: instructor
# Date: 2025
#
# data entry from entry widget
#

import tkinter as tk
#from tkinter import ttk

# obtain data entered by operator
def get_entry_value():
    value = entry_name.get ()
    print ("Entry value:", value)
    entry_name.delete(6, tk.END)

# create main window
# all window widgets must be defined before the call to mainloop()
root = tk.Tk ()
root.title ("Entry Box Data Retrieval")
root.geometry ("300x150")


# create a label and entry widget(s) -- text method
# 
tk.Label (master=root, text="Value").pack()


# create a string var class object
# this variable will store the data entered by the user
nameText = tk.StringVar()

# create the entry class object
entry_name = tk.Entry (root, width=25, textvariable=nameText)
entry_name.insert (0, "Name: ")
entry_name.pack ()

#create button to know when to read data
button = tk.Button (root, text="Click to accept", command=get_entry_value)
#button = ttk.Button (root, text="Click to accept", command=get_entry_value)
button.pack ()


# display the GUI and enter event processing loop
root.mainloop()

