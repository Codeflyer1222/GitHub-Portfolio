#!/usr/bin/env python3
#
# Problem: Are multiple windows supported
# Author: instructor
# Date: 1 April 2026
#
# File: 
#      1. multipleWindows.py - this file
#
# basic window start
import tkinter as tk

def get_entry_value (event):
    value = entry_name1.get ()
    print ("Entry value from Window 1: ", value)

def get_entry_value2 (event):
    value = entry_name2.get ()
    print ("Entry value from window 2: ", value)

# create main window
# all window widgets must be defined before the call to mainloop()
root = tk.Tk ()
root.title (" Window #1 ")
root.geometry ("400x400")

# create a 2nd window
root2 = tk.Tk ()
root2.title (" Window #2 ")
root2.geometry ("400x400")

# create a frame associated with Window 1 (root)
# Make the window an entry box
#
label1 = tk.Label (root, text="Value")
entry_name1 = tk.Entry ()
label1.pack ()
entry_name1.pack ()
entry_name1.bind ("<Return>", get_entry_value)

# create a frame associated with Window 2 (root2)
# Make the window an entry box
#
label2 = tk.Label (root2, text="Value")
entry_name2 = tk.Entry (master=root2)
label2.pack ()
entry_name2.pack ()
entry_name2.bind ("<Return>", get_entry_value2)

# display the GUI and enter event processing loop
root.mainloop()
root2.mainloop()
