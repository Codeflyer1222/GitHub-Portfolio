#!/usr/bin/env python3
#
# Problem: Temperature Converter GUI
# Files:
# 
#
# Author: Samuel Brown
# Date: 16 April 2026

#The star means import everything from tkinter
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


#function for button to convert celcius to fahrenheit
def celsius_to_fahrenheit_conversion():
    try:
        #gets user's text
        temp_c = float(entry_box_one.get())
        #formula for getting fahrenheit from celcius
        temp_f = temp_c * 9 / 5 + 32
        #updates the bottom label/conclusion
        result_label.config(
            text=f"{temp_c:.2f}° C = {temp_f:.2f}° F"
        )
    #error handling if user doesn't type a number
    except ValueError:
        showerror("Invalid Input", "Please enter a numeric value.")

#function to convert fahrenheit to celcius
def fahrenheit_to_celsius_conversion():
    try:
        #gets user's text
        temp_f = float(entry_box_two.get())
        #formula for getting celcius from fahrenheit
        temp_c = (temp_f - 32) * 5 / 9
        #updates the bottom label/conclusion
        result_label.config(
            text=f"{temp_f:.2f}° F = {temp_c:.2f}° C"
        )
    #error handling if user doesn't type a number
    except ValueError:
        showerror("Invalid Input", "Please enter a numeric value.")




# all window widgets must be defined before the call to mainloop()
#create window
root = tk.Tk()

root.title("Temperature Converter")

root.geometry("600x300")


#label prompting Celcius to Fahrenheit entry box
label_one = ttk.Label (root, text="Input Celsius:")
label_one.grid (padx=5, pady=5, column=0, row=0)

#entry box widget for Celcius to Fahrenheit
entry_box_one = ttk.Entry (root, width=25)
entry_box_one.grid (padx=5, pady=5, column=1, row=0)

#button to perform conversion
button_one = ttk.Button (root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit_conversion)
button_one.grid (padx=5, pady=5, column=2, row=0)



#label prompting Fahrenheit to Celcius entry box
label_two = ttk.Label (root, text="Input Fahrenheit:")
label_two.grid (padx=5, pady=5, column=0, row=1)

#entry box widget for Fahrenheit to Celcius
entry_box_two = ttk.Entry (root, width=25)
entry_box_two.grid (padx=5, pady=5, column=1, row=1)

#button to perform conversion
button_two = ttk.Button (root, text="Convert to Celcius", command=fahrenheit_to_celsius_conversion)
button_two.grid (padx=5, pady=5, column=2, row=1)


result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.grid(padx=5, pady=10, column=0, row=2, columnspan=3)


root.mainloop ()
