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
'''
# import random module
import random

# Usable characters
characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_!@#$%^&*()></?'

length = 10 # password length

while True: # loop until password length
    if input("Press <Enter> for your password or any key to exit: "): # press "enter" key to generate a password
        break # end if not "enter" key
    password = ''.join([random.choice(characters) # generate random password length from letters list 
                        for _ in range(length)])
    print(f"Your password is: {password}")