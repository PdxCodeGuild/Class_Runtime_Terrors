#!/bin/python3
# Filename: lab_09_3_unit_converter.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 13: Unit Converter - Version 3
# Date: 10/13/2020
# Version 1.0


'''
Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m

feet = {'meters': '0.3048'} # Dictionary value  
conversion = feet['meters'] # input for feet
feet = input('To convert feet to meters, enter feet: ') # user input in feet
feet = float(feet) # float conversion
conversion = float(conversion) # float conversion
answer = conversion * feet # result of feet to meter calculation
print (f'{feet:.2f} feet is equal to {answer:.2f} meters.') # print results

'''
# key: values,
conversion = {'ft': '0.3048', 'mi': '1609.34', 'm': '1', 'km': '1000'}

while True:
 distance = input('what is the distance? ')
 units = input('what are the units (ft, mi, m, km)? ')
 
 # feet 
 if units == 'ft':
  feet = (conversion['ft'])
  feet = float(feet)
  distance = float(distance)
  results = (feet * distance)
  print(distance, 'feet is equal to ', results, 'meter')

 # miles 
 elif units == 'mi':
  miles = (conversion['mi'])
  miles = float(miles)
  distance = float(distance)
  results = (miles * distance)
  print(distance, 'miles is equal to ', results, 'meters')

 # meters 
 elif units == 'm':
  meters = (conversion['m'])
  meters = float(meters)
  distance = float(distance)
  results = (meters * distance)
  print(distance, 'meters is equal to ', results, 'meters')

 # kilometers 
 elif units == 'km':
  kilometers = (conversion['km'])
  kilometers = float(kilometers)
  distance = float(distance)
  results = (kilometers * distance)
  print(distance, 'kilometers is equal to ', results, 'meters')

 another = input('Convert another? (yes/no) ')
 if another == 'yes':
  continue
 else:
   break