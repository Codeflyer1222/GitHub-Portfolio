#!/usr/bin/env python3
#
# Problem: <tkinter frame with label demonstration>
# Author: instructor
# Date: 2025
#
# File: GUIFrameLabel.py
# basic window start
#
# import modules
import tkinter as tk

# create main window
# all window widgets must be defined before the call to mainloop()
root = tk.Tk ()
root.title ("Hello World")
root.geometry ("300x150")
"""
# create a frame
#
frame1 = tk.Frame (root, width=100, height=100, bg="red")
frame2 = tk.Frame (root, width=50, height=50, bg="green")
frame3 = tk.Frame (root, width=25, height=25, bg="white")
"""
# The following uses hexadecimal codes
# Note: on some systems white = 000000
#

frame1 = tk.Frame (root, width=100, height=10, bg="#FF0012")
frame2 = tk.Frame (root, width=50, height=10, bg="#00FFe0")
frame3 = tk.Frame (root, width=25, height=10, bg="#f7f7f7")

# create a label
# 
label1 = tk.Label (master=frame1, text="label 1 in frame 1")
label1.pack()

label2 = tk.Label (master=frame2, text="Label 2 in Frame 2", fg="red", bg="white")
label2.pack()

label3 = tk.Label (master=frame3, text="Label 3 in Frame 3", fg="green", bg="red")
label3.pack()
"""
frame1.pack (fill=tk.BOTH, expand=True)
frame2.pack (fill=tk.BOTH, expand=True)
frame3.pack (fill=tk.BOTH, expand=True)
"""
frame1.pack (expand=True)
frame2.pack (expand=True)
frame3.pack (expand=True)

# display the GUI and enter event processing loop
root.mainloop()
