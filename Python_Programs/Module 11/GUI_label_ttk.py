#!/usr/bin/env python3
#
# Problem: <tkinter ttk label demonstration>
# Author: instructor
# Date: 2025
#
# display a tkinter.ttk labeled window
#      to show the differences between tk and ttk
#
# import required modules
# 
import tkinter as tk
from tkinter import ttk     # tk is the themed widget set

# all window widgets must be defined before the call to mainloop()
# create main window
# by convention the root window variable is called root
root = tk.Tk ()
print ("The type of root is ", type (root))
root.title ("First GUI Program")

# Create a label widget
ttk_label = ttk.Label (root, text="This is a tkInter label")
ttk_label.pack ()

# Create an entry widget
ttk_entry = ttk.Entry (root)
ttk_entry.pack ()

# Create a button widget
ttk_button = ttk.Button (root, text="Click Me")
ttk_button.pack ()

# the geometry method sets the width and height of the window
# by default the width and height are given in pixels
root.geometry ("300x150")

# display the GUI and enter event processing loop
root.mainloop()


