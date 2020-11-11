#!/bin/python3
# Filename: lab1_1_1_make_change.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 11: Make Change - Version 1
# Date: 10/18/2020
# Version 1.0

'''
Let's convert a dollar amount into a number of coins. 
The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. 
Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Welcome to the Change Maker 5000 (tm)
Enter a dollar amount: 1.36
5 quarters, 1 dime, and 1 penny
Would you like make more change? yes
Enter a dollar amount: 0.67
2 quarters, 1 dime, 1 nickel, 2 pennies
Would you like make more change? no
Have a good day!

'''

# pseudo code
'''
Print welcome message
Define conversion value
User input amount
Convert user input amount to coin value
Print coin value
Ask to make more changes
If yes, loop to start
If no, end

'''

# User input amount
def usr_input():
    while True:
                  i = input('Enter a dollar amount: ')
                  try:
                                    i = float(i)    
                                    return (i)
                  except:
                                    print('Try again.')

# Ask to make more changes
def do_again():
    while True:
                  do_again = input('Would you like make more change: Y or N: ')
                  if do_again == 'Y': # If yes, loop to start
                                    return True
                  elif do_again == 'N': # If no, end
                                    return False
                  else: # Wrong entry
                                    print('Try again.')

# Define conversion value
def main(): 
    while True:
                  amount = usr_input()
                  value = amount
                  qtr = value // .25
                  value = value - qtr * .25
                  dime = value // .10
                  value = value - dime * .10
                  nickel = value // .05
                  value = (value - nickel * .05) *100
                  value = round(value)

# Convert user input amount to coin value and Print coin value
                  if qtr > 1:
                                    print (f'{int(qtr)} Quarter/s' )
                  if dime > .1:
                                    print (f'{int(dime)} Dime/s ')
                  if nickel > .05:
                                    print (f'{int(nickel)} Nickle/s ')
                  if value >= 1:
                                    print (f'{value} Penny/ies ')
                  if do_again() == False:
                                    break

# Print welcome message
print('Welcome to the Change Maker 5000 (tm)')
main()

# Print leaving message
print('Have a good day!')