class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        self.p = 2 * (self.length + self.width)
        return self.p

    def area(self):
        self.a = (self.length * self.width)
        return self.a
    
    def display(self):
        self.perimeter()
        self.area()
        print (f'The length of the rectangle is {self.length} and the width is {self.width}')
        print (f'The parimeter of the rectangle is {self.p}')
        print (f'The area of the rectangle is {self.a}')

dimensions = Rectangle(10, 5)
dimensions.display()

class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        self.v = (self.length * self.width * self.height)
        print (f' The volume is {self.v}')

shape = Parallelepipede(77, 5, 12)
shape.volume()