# 2nd file

# =================================================================================
# 10/14/2020


# IF
# temperature = 69

# if temperature < 90:
#     if 60 < temperature <70:
#         print ('hot')
#     elif 68 < temperature < 80:
#         print('heally hot')
# elif temperature <60:
#     print ('Cold')

# def has_elements(nums):
#     return nums is not None and len(nums) > 0

# print (has_elements(None))


# # slicinging
# text = "hello world"

# print(text[0:5])
# print(text[5:10])
# print(text[::2]) # Ski ping every 2
# print(text[0:6:2]) # First 2 is Range and 3rd is the ship starting from 0



# x = 5
# print(id(x))
# x = 6
# print(id(x))

# =================================================================================
# 10/15/2020
# Peduacode 
#list review
#you can have mix list, example a list in a list.
# Dont use is, use with == can compare list with list,
#you need to aim the to get a list in a list Using ::: is slicing 
#List and Tupe https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
#to copy list new_list = list.copy() use the copy.()
# append() Parameters
# The method takes a single argument

# item - an item to be added at the end of the list
# The item can be numbers, strings, dictionaries, another list, and so on.
#pop remove the new one. and remove what you want
#extend is joinine two list toget

# tuples are ummute used to save data
# list are

#unpacking
#x = (a,b,c)
# (va, vb, vc) = x
# #


# get the index number
# listx = ['a', 'b','c']
# for x in listx:
#     x1 = listx.index(x)
#     print(x1)

# --------------------10/16/2020
# fuctions 


# *args running muti times keys
# **kwargs data
#  read up!
# 10/19/2020 Notes
# fuctions
#Read up global vars ex. global x

# raise Exception ('Sorry)
# try and eccept and finally

#lambda  x: 3 +1  one line funtion
# fn.strip().tittle()
#look at strip

# full_name = lambda fn, ln : fn.strip().title() + " " + ln.strip().title()
# # print(full_name("Eric" , "le"))

# # -----------------------------10/20/2020 notes 
# Sending a GET Request
# Sending a GET request is the direct equivalent of using your browser, you can get the body of the response using response.text.

# import requests

# response = requests.get('https://api.ipify.org')

# data = response.json() reform
# print(response.text) # 76.105.187.182
# api


class Employee:
 raise_amount = 1.04
 def __init__(self, first,last ,pay):
   self.first = first
   self.last = last
   self.pay = pay
   self.email = first + "." + last + "@gmail.com"
 def fullname(self):
   return self.first + ' ' + self.last
 def apply_raise(self):
   self.pay = int(self.pay * self.raise_amount)
   return self.pay
class Developer(Employee):
 raise_amount = 1.10
 def __init__(self, first,last,pay, prog_language):
   super().__init__(first,last,pay)
   self.prog_language = prog_language
class Manager(Employee):
   def __init__(self, first,last,pay, employees=None):
     super().__init__(first,last,pay)
     if employees is None:
       self.employees = []
     else:
       self.employees = employees
   def add_emp(self, emp):
     if emp not in self.employees:
       self.employees.append(emp)
   def remove_emp(self, emp):
     if emp in self.employees:
       self.employees.remove(emp)
   def print_emps(self):
     for emp in self.employees:
       print('===>', emp.fullname())
dev_1 = Developer('alex', 'd', 50, 'python')
dev_2 = Developer('Bruce', 'Wayne', 60, 'java')
mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])
# print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()