#!/bin/python3
# Filename: lab_09_2_unit_converter.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 13: Unit Converter - Version 2
# Date: 10/13/2020
# Version 1.0


'''
Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. 
So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m
'''

metric = {'meters': '0.3048'} # Dictionary value  
conversion = metric['meters'] # input for metric
feet = input('To convert meters to feet, enter feet: ') # user input in feet
feet = float(feet) # float conversion
conversion = float(conversion) # float conversion
answer = conversion * feet # result of feet to meter calculation
print (f'{feet:.2f} feet is equal to {answer:.2f} meters.') # print results
