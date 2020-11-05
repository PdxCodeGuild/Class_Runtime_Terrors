# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
# Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped.

# Exercise number 2)
# a) Import datetime
# b) Create a class with the following attributes:
# name
# last name
# surname
# address
# age
# telephone
# email
# Create a method that based on today’s time can return the person’s age. For instance, if this person was born in (1992, 3, 12) and I use this method, I should get 28 as a result

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self): #Area
        self.area = self.length * self.width
        return self.area
    def display (self):
        s ="Your Lenght was " + str(self.length) +", your width was "+ str(self.width) +" giving you an Area of "+ str(self.area)
        return s
class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    def Volume(self):
        self.volume = self.length * self.width *self.height
        return self.volume
    def display2 (self):
        s ="Your Lenght was " + str(self.length) +", your width was "+ str(self.width) +", your height  was "+ str(self.height) +" giving you an Volume of "+ str(self.volume)
        return s

print('Exercise 1 Area/Volume')

rlength = int(input('What is the Lenght: '))
rwidth = int(input('What is the Weidth: '))
rheight = int(input('What is the Height: '))

rRectangle = Rectangle(rlength, rwidth)
rPar = Parallelepipede(rlength, rwidth, rheight)
rRectangle.Perimeter()
rPar.Volume()

print(rRectangle.display())
print(rPar.display2())