#!/bin/python3
# Filename: lab06_2-random_password.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 6: Password Generator - Version 2
# Date: 10/14/2020
# Version 1.0

'''
Allow the user to enter the value of n, remember to convert its type, as input returns a string.
'''

# import random module
import random

pwd = []
# Usable characters
characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_!@#$%^&*()></?'
characters = list(characters) #Making into a list

# User input for password length
password_length = int(input('Enter how many characters you want for your password length? '))

# Starting at zero
i = 0

# Number of characters from user input
while i < password_length: # If password generated is les than User input, continue
  i+=1
  choice = random.choice(characters)
  pwd.append(choice)

# Combine all generated characters
pwd = ''.join(pwd)

# Print password
print(f"Your password is: {pwd}")