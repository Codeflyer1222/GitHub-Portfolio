#!/usr/bin/env python3
#
# Problem: <tkinter label demonstration>
# Author: instructor
# Date: 2025
#
# display a tkinter labeled window
#
# import required modules
import tkinter as tk

# all window widgets must be defined before the call to mainloop()
# create main window
# by convention the root window variable is called root
root = tk.Tk ()
print ("The type of root is ", type (root))
root.title ("First labeled Window")

# Create a label widget
win_label = tk.Label (root, text="This is a tkInter label")
#NEEDS .pack FOR EVERY CHANGE TO WINDOW
win_label.pack ()

# Create an entry widget
win_entry = tk.Entry (root)
win_entry.pack ()

# Create a button widget
win_button = tk.Button (root, text="Click Me")
win_button.pack ()

# the geometry method sets the width and height of the window
# by default the width and height are given in pixels
root.geometry ("300x150")

# display the GUI and enter event processing loop
root.mainloop()


