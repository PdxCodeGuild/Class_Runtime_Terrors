# 10/27 Note: 
# class Employee:
#  raise_amount = 1.04
#  def __init__(self, first,last ,pay):
#    self.first = first
#    self.last = last
#    self.pay = pay
#    self.email = first + "." + last + "@gmail.com"
#  def fullname(self):
#    return self.first + ' ' + self.last
#  def apply_raise(self):
#    self.pay = int(self.pay * self.raise_amount)
#    return self.pay
# class Developer(Employee):
#  raise_amount = 1.10
#  def __init__(self, first,last,pay, prog_language):
#    super().__init__(first,last,pay)
#    self.prog_language = prog_language
# class Manager(Employee):
#    def __init__(self, first,last,pay, employees=None):
#      super().__init__(first,last,pay)
#      if employees is None:
#        self.employees = []
#      else:
#        self.employees = employees
#    def add_emp(self, emp):
#      if emp not in self.employees:
#        self.employees.append(emp)
#    def remove_emp(self, emp):
#      if emp in self.employees:
#        self.employees.remove(emp)
#    def print_emps(self):
#      for emp in self.employees:
#        print('===>', emp.fullname())
# dev_1 = Developer('alex', 'd', 50, 'python')
# dev_2 = Developer('Bruce', 'Wayne', 60, 'java')
# mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])
# # print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

###### Exercise Number 1 #######
# class Rectangle():
#     def __init__(self, length = 0, width = 0, perimeter = 0, area = 0): # set default value if user not input it
#         self.length = length
#         self.width = width
#         self.perimeter = (self.length + self.width) * 2
#         self.area = self.width * self.length
#     def Perimeter(self):
#         return (self.length + self.width) * 2
#     def Area(self):
#         return self.width * self.length
#     def Display(self):
#         return(print(f"length = {self.length}, width = {self.width}, perimeter = {self.Perimeter()}, and area = {self.Area()}"))


# class Parallelepipede(Rectangle):
#     def __init__(self, length, width, perimeter, area, height):
#         super().__init__(length, width, perimeter, area)
#         self.height = height # define the additional attribute
#     def Volume(self):
#         return print(self.length * self.width * self.height)

# shape_1 = Rectangle(2,3)
# volume_1 = Parallelepipede(2,3,0,0,4)
# volume_1.Volume()

####### Exercise 2 #######
# Create a method that based on today’s time can return the person’s age
# For instance, if this person was born in (1992, 3, 12) and I use this method,
# I should get 28 as a result

import datetime

class Database():
    def __init__(self, lastname, surname, name = "", address ="", age = 0, telephone = "", email = ""):
        self.lastname = lastname
        self.surname = surname
        self.name = self.lastname + ' ' + self.surname
        self.address = address
        self.age = age
        self.telephone = telephone
        self.email = email 

