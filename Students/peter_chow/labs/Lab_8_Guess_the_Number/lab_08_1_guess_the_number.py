#!/bin/python3
# Filename: lab_08_1_guess_the_number.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 8: Guess the Number - Version 1
# Date: 10/15/2020
# Version 1.0

'''
Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost. 
If the user guesses the number, the user is told they've won and the game exits. You can get a random number using random.randint:

'''
# pseudo code
'''
Import random
Computer generates at random int betweek 1 and 10
input Guess the Number:
Compaire random to guess numbers
Print results
Loop to try again if wrong
Print if correct
'''

import random
# Computer generates at random int betweek 1 and 10
cpu = random.randint(1,10)

# Set count 
num_guess = 0

# Enter user number
while num_guess < 10:
    print('Guess a number between 1 and 10: ') 
    guess = input()
    guess = int(guess)
    num_guess = num_guess + 1 # Number of try count down

    if guess != cpu: # Wrong guess
        print('Try again! ')  

    if guess == cpu: # Correct guess, continue
        break

if guess == cpu: # Guess correct, print message
    num_guess = str(num_guess)
    print('You won! The number was: ' + num_guess)

if guess != cpu: # Guess incorrect, print message
    cpu = str(cpu)
    print('Nope. The number was: ' + cpu)