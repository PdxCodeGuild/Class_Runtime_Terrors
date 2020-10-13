



# function - a block of code that takes parameters and returns a value
# method - a special kind of function that belongs to a class

# s = 'hello world'
# words = s.split(' ')


# import random
# print(random.choice('abc'))

# import module_example
# # from .module_example import add
# print(module_example.add(5, 2))

import json
contact = {'name': 'bob', 'age': 55}
contact_json = json.dumps(contact)
print(contact_json)
contact = json.loads(contact_json)
print(contact)


exit()



import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    
    def scale(self, v):
        self.x *= v
        self.y *= v


p = Point(5, 2)
print(p.x)
print(p.y)

exit()


# print('start program')
# p1 = Point(5, 2) # this creates an instance of our class, instantiation
# p2 = Point(8, 4)

# HERESEY - adding a new property outside the initializer
# p1.message = 'hello'
# print(p1.message)

# print('p1', p1)
# print('p2', p2)
# print(p1.distance(p2))
# print(Point.distance(p1, p2)) # HERESEY - invoking a method using the class







# OOP - object-oriented programming
# thinking of a program in terms of objects and their relationships
# instead of thinking of it as a bunch of functions

# three pillars of OOP
# encapsulation - hiding the internals of a class, specifying an interface by which other code can use the class
# inheritance - deriving a type from another type
# polymorphism - the ability of a type to be used like another type



# Encapsulation =======================

import math

class Point:
    def __init__(self, x, y):
        self.__x = x # private variable
        self.__y = y
    
    def distance(self, p): # method, or 'member function'
        dx = self.__x - p.__x
        dy = self.__y - p.__y
        return math.sqrt(dx*dx + dy*dy)
    
    def scale(self, v):
        self.__x *= v
        self.__y *= v
    
    # 'getters'
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    # 'setters'
    def set_x(self, x):
        self.__x = x
    
    def set_y(self, y):
        self.__y = y


# p1 = Point(5, 2)
# print(p1.get_x())
# p1.set_x(6)
# print(p1.get_x())
# # print(p1.__x) # AttributeError: 'Point' object has no attribute '__x'
# print(p1._Point__x) # HERESEY - accessing a private variable
# p2 = Point(8, 4)
# print(p1.distance(p2))


# dynamic vs static  typing ======================================

# dynamic typing - playdough =======================

# def add(a, b):
#     return a + b

# print(add(5, 2))
# print(add('a', 'b'))
# print(add({'a': 1}, {'b': 2})) # crash

# variables can change type
# x = 5
# x = 5.2
# x = 'llama'

# static typing - legos =======================

# int add(int a, int b) {
#     return a + b
# }
# add(5, 2)
# add('a', 'b') # crash - the function doesn't take strings

# variables cannot change type
# int x = 5
# x = 5.2 # crash - x is an int


# inheritance ===================================


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# person = Person('Mike', 54)
# print(person.name)

# Student is inheriting from Person
class Student(Person):
    def __init__(self, name, age, classes):
        super().__init__(name, age)
        self.classes = classes
    
# student = Student('Bobby', 12, ['math', 'history', 'english'])
# print(student.name)
# print(student.age)
# print(student.classes)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    

# teacher = Teacher('Janice', 45, 'math')
# print(teacher.name)
# print(teacher.age)
# print(teacher.subject)


# polymorphism =======================================

# you can write code that deals directly with the parent class
# regardless of what class the child is an instance of

# it doesn't matter whether this function is given a person, student, or teacher
def print_person(p):
    print(f'Name: {p.name}, age: {p.age}')

person1 = Student('Bobby', 12, ['math', 'history', 'english'])
person2 = Teacher('Janice', 45, 'math')

print_person(person1)
print_person(person2)



# class RandomOtherClass:
#     def __init__(self):
#         self.name = 'not actually a person'
#         self.age = 'not my age lol'
# print_person(RandomOtherClass())

