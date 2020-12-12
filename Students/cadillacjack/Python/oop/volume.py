class Volume:
    def __init__(self, length, width, height):
        self.length = int(length)
        self.width = int(width)
        self.height = int(height)
    def perimeter(self):
        per = 2 * (self.length * self.width)
        return per
    def area(self):
        area = self.length * self.width
        return area
    def vol(self):
        volu = self.length * self.width * self.height
        return volu


class All_measurements(Volume):
    def __init__(self, length, width, height):
        super().__init__(length, width, height)
        self.area = self.area()
        self.per = self.perimeter()
        self.volu = self.vol()
        
    def print_all(self):
        print(f'''
The Area is : {self.area}
The Perimeter is : {self.per}
The Volume is : {self.volu}''')

length = input("What is the length : ")
width = input("What is the width : ")
height = input("What is the height : ")

what_should_never = All_measurements(length, width, height)
what_is = Volume(length, width, height)
print(Volume.area(what_is))
print(Volume.perimeter(what_is))
print(Volume.vol(what_is))
print(All_measurements.print_all(what_should_never))