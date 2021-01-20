

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def perimeter(self):
        peri = (self.length + self.width) *2
        return peri

    def area(self):
        space = self.length * self.width
        return space

class Parallelepipede(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        zen = self.area() * self.height
        return(zen)

    def display(self):
        shape = input(f'Which shape do you wish to display,"para" or "rec"? ')
        if shape == 'para':
            print(f'''the shape is {self.length} long,
            {self.width} wide,
            {self.height} tall,
            and has a volume of {self.volume()}''')
        if shape == 'rec':
            print(f'''the shape is {self.length} long,
             {self.width} wide and 
             has an area of {self.area()}''')


rec_1 = Rectangle(20,30)
rec_2 = Rectangle(20,50)

para_1 = Parallelepipede(30,3,10)
para_2 = Parallelepipede(10,10,10)

print(para_1.width)

print(para_1.volume())

para_1.display()
para_2.display()