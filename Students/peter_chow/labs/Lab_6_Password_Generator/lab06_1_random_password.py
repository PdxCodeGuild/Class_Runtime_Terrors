#!/bin/python3
# Filename: lab06_1-random_password.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 6: Password Generator - Version 1
# Date: 10/14/2020
# Version 1.0

'''
Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

Concepts Covered
input, print
looping
random.choice
the 'sting builder pattern'

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