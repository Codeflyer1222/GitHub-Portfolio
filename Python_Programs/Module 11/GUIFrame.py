#!/usr/bin/env python3
#
# Problem: <tkinter frame demonstration>
# Author: instructor
# Date: 2025
#
# File: GUIFrame.py
# basic window start
#
import tkinter as tk

# create main window
# all window widgets must be defined before the call to mainloop()
root = tk.Tk ()
root.title (" Multiple Frames 1 window ")
root.geometry ("300x300")

# create a frame
# with specific rectangle size and color backround
#

frame1 = tk.Frame (root, width=100, height=100, bg="red")
frame2 = tk.Frame (root, width=50, height=50, bg="green")
frame3 = tk.Frame (root, width=25, height=25, bg="purple")

# create a frame
# with height only defined and color 
#
"""
frame1 = tk.Frame (root, height=100, bg="red")
frame2 = tk.Frame (root, height=50, bg="green")
frame3 = tk.Frame (root, height=25, bg="white")

frame1.pack ()
frame2.pack ()
frame3.pack ()
"""
#
# does not override the rectangle previously defined size
# 

frame1.pack (expand=True)
frame2.pack (expand=True)
frame3.pack (expand=True)
"""
# fill overrides width/height options
# expand = responsive to window size
frame1.pack (fill=tk.BOTH, expand=True)
frame2.pack (fill=tk.BOTH, expand=True)
frame3.pack (fill=tk.BOTH, expand=True)

frame1.pack (fill=tk.X, expand=True)
frame2.pack (fill=tk.X, expand=True)
frame3.pack (fill=tk.X, expand=True)
"""
# display the GUI and enter event processing loop
root.mainloop()
