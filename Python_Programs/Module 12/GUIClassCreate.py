#!/usr/bin/python
#
# GUICreateClass.py
# creating a frame class
# GUIClassCreate.py
# from  https://www.pythontutorial.net/tkinter/tkinter-object-oriented-frame/
# 
# 
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

# define inherited class
#
class myFrame (ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # define a dictionary for options
        options = {'padx': 5, 'pady': 5}

        #create label
        self.label = ttk.Label (self, text="Hello world")
        self.label.pack (**options)

        #create a button
        self.button = ttk.Button (self, text="Click me", command=self.button_clicked)
        #self.button['command'] = self.button_clicked
        self.button.pack (**options)

    def button_clicked (self):
        response = askyesno (title='Exit ?', message="do you want to end the program")
        if response == True:
            root.destroy()

class myWin (tk.Tk):
    def __init__(self):
        super().__init__()
        self.title ("My Awesome Class")
        self.geometry ("300x150")   

# create main window
# all window widgets must be defined before the call to mainloop()

#CREATE WINDOW 
root = myWin()
#CREATE WINDOW FRAME
frame = myFrame (root)
frame.pack ()

root.mainloop ()