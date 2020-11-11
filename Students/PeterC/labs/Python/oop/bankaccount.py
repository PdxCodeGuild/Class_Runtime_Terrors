#!/bin/python3
# Filename: bankaccount.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: BankAccount - Version 1
# Date: 10/26/2020
# Version 1.0

'''
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.
'''

class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def deposit(self, _in):
        return self.balance + _in
    def withdraw(self, _out):
        return self.balance - _out
    def bankFees(self):
        return self.balance - (self.balance * 0.05)
    def display(self):
        return self.accountNumber, self.name, self.balance

acct1 = BankAccount(10101010, 'Bill Gates', 110000000000)
acct2 = BankAccount(10101011, 'Steve Jobs', 10500000000)
print("\n\t\t  Account #       Name        Balance")
print("Starting Balances: =======================================")
print("\t\t",  acct1.display())
print("\t\t",  acct2.display())

acct1.balance = acct1.deposit(50000000)
acct2.balance = acct2.withdraw(85000000)
acct1.balance = acct1.bankFees()
acct2.balance = acct2.bankFees()
print("\n\n\t\t  Account #       Name        Balance")
print("Ending Balances: =========================================")
print("\t\t",  acct1.display())
print("\t\t",  acct2.display())