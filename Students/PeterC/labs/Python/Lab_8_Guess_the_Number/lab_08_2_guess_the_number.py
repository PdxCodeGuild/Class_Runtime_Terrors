#!/bin/python3
# Filename: lab_08_2_guess_the_number.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 8: Guess the Number - Version 2
# Date: 10/16/2020
# Version 1.0

'''
Allow the user to make an unlimited number of guesses using a while True and break. 
Keep track of how many guesses the user has made, and tell them at the end.

'''
# pseudo code
'''
Import random
input Guess the Number:
Compaire random to guess numbers
Count trys
Print results
Loop to try again if wrong
Print if correct and number of trys
'''

import random

# Computer generates at random int betweek 1 and 10
cpu = random.randint(1,10)

# Enter user number
def user_input():
    while True:
     cpu = input('Guess a number from 1 to 10: ')
     try:
          cpu = int(cpu) # Guess correct continue to print correct message 
          return (cpu)
     except: # Guess incorrect continue loop
          print()

# Count guess
def main():
    guesscount = 0
    guess = 0
    while True:
        if guess != cpu: # Guess incorrect 
            guesscount += 1 # Guess count
            guess =  user_input() # Guess correct, print message
            if guess != cpu: 
                print('Try again.') # Print Try again message
            else:
                break
  
    print(f'Correct! It took {guesscount} guesses.') # Guess correct, print message

main()