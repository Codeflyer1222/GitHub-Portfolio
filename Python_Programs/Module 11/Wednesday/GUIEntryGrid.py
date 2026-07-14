#!/usr/bin/env python3
#
# Problem: <tkinter entries on a grid demonstration>
# Author: instructor
# Date: 2025
#
# File: GUIEntryGrid.py
# data componenets on a grid
# 

import tkinter as tk

# create main window
# all window widgets must be defined before the call to mainloop()
root = tk.Tk ()
root.geometry ("500x500")

# create a labels 
# 
label1 = tk.Label (master=root, text="First: ")
label2 = tk.Label (master=root, text="Second: ")

# configure grid to arrange labels into
# rows and columens 
#sticky ALIGNS TEXT. TOP IS N, BOTTOM IS S, LEFT IS W...
#pady is PADDING
label1.grid (row=0, column=0, sticky=tk.W, pady=2)
label2.grid (row=1, column=0, sticky=tk.W, pady=2)

# create entry widgets, to get data from user
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

# arrange the entry grids
entry1.grid (row=0, column=1, pady=2)
entry2.grid (row=1, column=1, pady=2)

#checkbutton widget
button_check = tk.Checkbutton (root, text="Preserve")
button_check.grid (row = 2, column = 0, sticky=tk.W, columnspan = 2)

# add imgage
# image must be .png 
# subsample scales smaller but not larger
# 
#PhotoImage USES PNG AS AN IMAGE
python_logo = tk.PhotoImage (file = "psf-logo.png")
img = python_logo.subsample (2, 2)

# arrange image
# 
tk.Label (root, image=img).grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5)


#add zoom buttons
#
In_button = tk.Button (root, text = "Zoom in")
Out_button = tk.Button (root, text = "Zoom out")

#arrange button widgets
In_button.grid (row=2, column=2, sticky=tk.E)
Out_button.grid (row=2, column=3, sticky=tk.E)

# display the GUI and enter event processing loop
root.mainloop()

