#!/bin/python3
# Filename: lab_rot13_2.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab_Rot13 - Version 2
# Date: 10/23/2020
# Version 1.0

'''
Allow the user to input the amount of rotation used in the encryption. (ROTN)
'''
shift = 13 # ROT13 shift count

y = input("Enter word(s) to encrypt: ") # User input
x =(y.lower()) # Convert all inputs to lower character(s)

encrypt = "" 
for cr in x:
    if cr:
        org_index = ord(cr) - ord("a") # Starting character
        new_index = (org_index + shift) % 26 # Set index to 26
        new_chr = new_index + ord("a") # New order
        rot_chr = chr(new_chr) 
        encrypt = encrypt + rot_chr
    else:
        exit

print('Plain text:',x)
print('Encrypted text:',encrypt)