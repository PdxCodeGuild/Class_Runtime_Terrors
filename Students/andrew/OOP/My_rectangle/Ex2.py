import datetime

class Person():
    def __init__(self, name, last_name, address, age, telephone, email):
        self.name = name
        self.last_name = last_name
        self.surname  = last_name
        self.address = address
        self.age = age
        self.telephone =telephone
        self.email = email
        
    def birthday(self):
        today = datetime.datetime.today()
        birthyear = today.year - self.age
        print(f'You were born in the year {birthyear}')
        
        
        
        
p1 = Person('Drew', 'Babcock','123 main st', 41, "1324655555","drew@mymail.com")

my_int = 2



p1.birthday()