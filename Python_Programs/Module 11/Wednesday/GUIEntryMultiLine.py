#!/usr/bin/env python3
#
# Problem: <tkinter multi line entry display demonstration>
# Author: instructor
# Date: 2025
#
# data entry from entry widget
#
import tkinter as tk


# create main window
# all window widgets must be defined before the call to mainloop()
root = tk.Tk ()
root.title ("Entry Box Data Retrieval")
root.geometry ("300x200")

#CREATE A WIDGET, PACK A WIDGET PATTERN. IT HELPS WITH ORDER OF TXT THATS DISPLAYED
# create a label 
label = tk.Label (master=root, text="Statement of the Day")
label.config (font=("Courier", 14))
label.pack ()     # move this to after the text box to show where label is placed

# create text widget and specify size
TextBox = tk.Text(root, height=5, width=52)
#TextBox = tk.Text(root)           # tk decides size
TextBox.pack ()

# create a label 
# this label would be after the TextBox on the window vice above it 
label2 = tk.Label (master=root, text="Statement of the Day2")
label2.config (font=("Courier", 14))
label2.pack ()

statement = "Python is fun. \n It makes my head hurt"
# add statement to TextBox
# 1st argument is what "index" to start statement
#
TextBox.insert (tk.END, statement)

#create button for next text
#
b_next = tk.Button (root, text="Next")
b_next.pack()

b_exit = tk.Button (root, text = "Exit", command = root.destroy )
b_exit.pack ()

# display the GUI and enter event processing loop
root.mainloop()

