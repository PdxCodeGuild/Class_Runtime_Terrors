import math
class D_Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def perimeter(self):
        return 2*(self.length + self.width)
    
    
    def area(self):
        return self.length * self.width
    
    def display(self):
        area  = self.area()
        perimeter = self.perimeter()
        print(f'The area is: {area}')
        print(f'The perimeter is: {perimeter}')
        
    
    
class Parallelpipede(D_Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        
    def volume(self):
        length = self.length
        width  = self.width
        height = self.height
        v = abs(abs(self.length * self.width)* height)
        
        print(f'The valume of this parallpiped is: {v}')
        
    



rect1 = D_Rectangle(3,4)

rect1.display()

parall1 = Parallelpipede(3,4,7)

parall1.volume()
