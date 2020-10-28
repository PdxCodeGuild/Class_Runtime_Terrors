#PDX Code Guild excercise OOP : exercise 1
# x   Write a Rectangle class in Python language, allowing you 
#       to build a rectangle with length and width attributes.
# x  Create a Perimeter() method to calculate the perimeter of 
#       the rectangle and a Area() method to calculate the area 
#       of ​​the rectangle.
#    Create a method display() that display the length, width, 
#       perimeter and area of an object created using an 
#       instantiation on rectangle class.
#    Create a Parallelepipede child class inheriting from the 
#       Rectangle class and with a height attribute and another 
#       Volume() method to calculate the volume of the 
#       Parallelepiped.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        self.perimeter = (self.width * 2) + (self.length * 2)
        return(self.perimeter)
    def area(self):
        self.area = (self.width * self.length)
        return(self.area)
    def display(self):
        return(self.length, self.width, self.perimeter(), self.area())

class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        self.volume = ((self.length * self.width) * self.height)
        return(self.volume)
    def display(self):
        return(self.length, self.width, self.height, self.perimeter(), self.area(), self.volume())

rect_1 = Rectangle(2, 4)
print(rect_1.display())

para_1 = Parallelepipede(2, 4, 3)
print(para_1.display())

