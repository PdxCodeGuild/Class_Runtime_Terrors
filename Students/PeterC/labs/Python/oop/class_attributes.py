#!/bin/python3
# Filename: class_attributes.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Create a class - Exercise number 2
# Date: 11/03/2020
# Version 1.0

'''
Exercise number 2)
a) Import datetime
b) Create a class with the following attributes:
name
last name
surname
address
age
telephone
email
Create a method that based on today’s time can return the person’s age. 
For instance, if this person was born in (1992, 3, 12) and I use this method, I should get 28 as a result

'''
from datetime import date, datetime, timedelta

class Attributes:
    global today
    def __init__(self, name, surname, address, birthday, phone):
        self.name = name
        self.surname = surname
        self.address = address
        self.birthday = birthday
        self.phone = phone
        self.email = self.name + '.' + self.surname + "@gatesfoundation.org"
    def age(self):
        self.birthday = datetime((int(self.birthday[0])), (int(self.birthday[1])), (int(self.birthday[2])))
        self.age = ((today.year - self.birthday.year) - ((today.month, today.day) <  (self.birthday.month, self.birthday.day)))
        return((self.age))
    
today = datetime.now()
info = Attributes('Bill', 'Gates', '1835 73rd Ave NE, Medina, WA 98039', (1955, 10, 28), '206-709-3100')
# print name, surname, and email
print(f'{info.name} {info.surname} email is: {info.email}')
# print age as of today
print(f'He is {info.age()} years old as of {today}')
# print address
print(f'{info.name} live at: {info.address}')