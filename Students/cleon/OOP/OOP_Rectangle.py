#Cleon 
#OOP Rectangle Lab
#10-27-2020


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def Perimeter(self):
        return ((self.length * 2) + (self.width * 2))
    def Area(self):
        return self.length * self.width
    def Display(self):
        print(f" Length = {self.length}\n Width = {self.width}\n Perimeter  = {self.Perimeter()}\n Area = {self.Area()} ")


class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__( length, width)
        self.height = height
    def volume(self):
        return self.Area() * self.height

    
thing_1 = Rectangle( 2,4)
thing_1.Display()


thing_2 = Parallelepipede(2,4,6)
print(f"The volume of thing 2 is {thing_2.volume()}")
