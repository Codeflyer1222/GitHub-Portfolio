#!/usr/bin/env python3
#
# Problem: <tkinter multi line entry retrival demonstration>
# Author: instructor
# Date: 2025
#
# data entry from entry widget
#
import tkinter as tk

def get_statement_from_user ():
    # Review a statement from the user
    # Grab everything except the newline character
    statement = TextBox.get ("1.0", "end-1c")
    print ("The statement is ", statement)
    print ("This is the end of function")

# create main window
# all window widgets must be defined before the call to mainloop()
root = tk.Tk ()
root.title ("Entry Box Data Retrieval")
root.geometry ("300x200")

# create a label 
label = tk.Label (master=root, text="Provide a statement")
label.config (font=("Courier", 14))
label.pack ()

# create text widget and specify size
TextBox = tk.Text(root, height=5, width=52)
# TextBox = tk.Text(root)           # tk decides size
TextBox.pack ()


#create button for next text
#
b_next = tk.Button (root, text="Get Text", command=get_statement_from_user)
b_next.pack()

b_exit = tk.Button (root, text = "Exit", command = root.destroy )
b_exit.pack ()



# display the GUI and enter event processing loop
root.mainloop()