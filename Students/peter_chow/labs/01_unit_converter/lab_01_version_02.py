#!/bin/python3
# Filename: lab_01_version_02.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 9: Unit Converter - Version 2
# Date: 10/13/2020
# Version 1.0


'''
Allow the user to also enter the units. Then depending on the units, convert the distance into meters. 
The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
'''
 
# key: values,
conversion = {'ft': '0.3048', 'mi': '1609.34', 'm': '1', 'km': '1000'}

while True:
 distance = input('what is the distance? ')
 units = input('what are the units (ft, mi, m, or km)? ')
 
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