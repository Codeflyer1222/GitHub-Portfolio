#!/usr/bin/env python3
#
# Problem: Bank Account ATM deposit code
# Author: instructor
# Date: 2025
#
# File: 
#      GUIBankATM.py - main loop
#      BankAccount.py - BankAccount Class definition
# 
class BankAccount:
    def __init__(self, account_number, pin, initial_balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        else: 
            print ("Withdraw can not be made")
            return False

    def get_balance(self):
        return self.balance
    
