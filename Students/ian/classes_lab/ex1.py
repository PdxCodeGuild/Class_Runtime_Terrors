"""
Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate 
the volume of the Parallelepiped.
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return (self.length + self.width) * 2

    def Area(self):
        return self.length * self.width

    def display(self):
        print(
            f"length: {self.length}\nwidth: {self.width}\nperimeter: {self.Perimeter()}\narea: {self.Area()}"
        )


r = Rectangle(2, 2)
r.display()


class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def Volume(self):
        return self.Area() * self.height


p = Parallelepiped(2, 2, 2)
print(p.Volume())
