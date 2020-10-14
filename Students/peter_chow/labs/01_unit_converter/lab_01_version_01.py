#!/bin/python3
# Filename: lab_01_version_01.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 9: Unit Converter - Version 1
# Date: 10/13/2020
# Version 1.0

'''
Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters. 
Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.
'''

ft = input('Enter Feet ')
print(ft, 'Feet is equal to', int(ft) * 0.3048, 'meters')