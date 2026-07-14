#!/usr/bin/env python3
#
# Problem: Bank Deposit / Withdraw GUI
# Author: instructor
# Date: 2025
#
# File: 
#       GUI_BankATM.py - this file
#       BankAccountclass.py - defines the BankAccount Class
# 

import tkinter as tk
import BankAccountClass


def make_deposit ():
    """ make a deposit to the account """
    value = float (entry_amount.get ())
    cust_account.deposit (value)
    print (f"current balance: {cust_account.get_balance ():.2f}")

def make_withdrawl ():
    """ make a withdrawl to the account """
    value = float (entry_amount.get ())
    cust_account.withdraw (value)
    print (f"current balance: {cust_account.get_balance ():.2f}")

#create an account
cust_account = BankAccountClass.BankAccount ("12345", 9087)

# create main window
# all window widgets must be defined before the call to mainloop()
root = tk.Tk ()
root.title ("ATM Demo")
root.geometry ("300x150")

# create a label and entry widget(s) -- text method
value_label = tk.Label (master=root, text="Enter Amount").pack()


# create the entry class object
entry_amount = tk.Entry (root, width=25)
entry_amount.pack ()

#create button to know when to read data
deposit_button = tk.Button (root, text="Click to deposit funds", command=make_deposit)
withdrawl_button = tk.Button (root, text="Click to withdrawl funds", command=make_withdrawl)
deposit_button.pack ()
withdrawl_button.pack ()

# display the GUI and enter event processing
root.mainloop()