#!/usr/bin/env python3
#
# Problem: <tkinter root window demonstration>
# Author: instructor
# Date: 2025
#
# basic window start
#
import tkinter as tk

# all window widgets must be defined before the call to mainloop()
# create main window
# by convention the root window variable is called root
root = tk.Tk ()
print ("The type of root is ", type (root))
root.title ("First GUI Program")

# the geometry method sets the width and height of the window
# by default the width and height are given in pixels
root.geometry ("300x150")

# display the GUI and enter event processing loop
root.mainloop()


