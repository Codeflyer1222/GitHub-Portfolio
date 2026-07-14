#!/usr/bin/python
#
# Problem: <tkinter button demonstration>
# Author: instructor
# Date: 2025
#
# File: GUIButton.py
#
# import tkinter module
import tkinter as tk

# When the button 1 is clicked the title changes to "Button clicked"
def b1_click ():
    root.title ("Button Clicked")

# when button 2 is clicked the program is ended
def b2_click ():
    root.destroy()

# create main window
# all window widgets must be defined before the call to mainloop()
root = tk.Tk ()
root.title ("Hello World")
root.geometry ("300x150")

# create two frames
frame1 = tk.Frame (root, width=100, height=100, bg="red")
frame1.pack (fill=tk.BOTH, expand=False)
#frame1.pack (fill=tk.BOTH, expand=True)

frame2 = tk.Frame (root, width=100, height=100, bg="blue")
frame2.pack (fill=tk.BOTH, expand=True)

# create a label
# 
label1 = tk.Label (master=frame1, text="Label 1", fg="white", bg="green")
label1.pack()

# create a button
#command IS A COMMAND TO RUN A FUNCTION
button = tk.Button (frame2, text="Click me!", bg="orange", fg="white", width=25, height=5, command=b1_click)
button.pack()

button2 = tk.Button (frame2, text="Click here to end program", width=25, height=5, command=b2_click)
button2.pack()

# The following statements are to show the frame pack can occur either immediately following the frame or 
# after all widgets are identified

#frame1.pack (fill=tk.BOTH, expand=False)
#frame1.pack (fill=tk.BOTH, expand=True)

#frame2.pack (fill=tk.BOTH, expand=True)


# display the GUI and enter event processing loop
root.mainloop()
