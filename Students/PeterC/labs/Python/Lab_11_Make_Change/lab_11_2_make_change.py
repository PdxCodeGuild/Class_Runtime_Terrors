#!/bin/python3
# Filename: lab1_1_2_make_change.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 11: Make Change - Version 2
# Date: 10/18/2020
# Version 1.0

'''
Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom coins.

coins = [
    ('half-dollar', 50)
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

'''

# pseudo code
'''
Print welcome message
Define tuples value
Define conversion value
User input amount
Convert user input amount to coin value
Print coin value
Ask to make more changes
If yes, loop to start
If no, end

'''
# Define tuples value
coins = {
    'Half-dollar/s': 50,
    'Quarter/s': 25,
    'Dime/s': 10,
    'Nickel/s': 5,
    'Penny/ies': 1
}

# User input amount
def usr_input():
    while True:
        i = input('Enter a dollar amount: ')
        try: # Convert input to float
            i = float(i)    
            return(i)
        except: # If not, loop again
            print('Try again.')

# Ask to make more changes
def again():
    while True:
        try_again = input('Would you like make more change: Y or N: ')
        if try_again == 'Y': # If yes, loop to start
            return True
        elif try_again == 'N': # If no, end
            return False
        else:
            print('Try again.')

# Convert user input amount to coin value
def main():
    while True:
        usr_amt = usr_input()
        amt = usr_amt * 100
        for cs in coins:
            new_amt = (amt // coins[cs])
            if new_amt > 0:
                print (f'{new_amt} {cs} ') # Print coin value
            amt = amt - (new_amt * coins[cs])

        if again() == False:
            break

# Print welcome message
print('Welcome to the Change Maker 5000 (tm)')
main()

# Print leaving message
print('Have a good day!')