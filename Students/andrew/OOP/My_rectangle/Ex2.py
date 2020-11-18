import datetime

class Person():
    def __init__(self, name, last_name, address, telephone, email):
        self.name = name
        self.last_name = last_name
        self.surname  = last_name
        self.address = address
        self.telephone =telephone
        self.email = email
        self.birthdate  = input("Please enter your birthday in yyyy-mm-dd formay")
        
  
        
        
        
        
p1 = Person('Drew', 'Babcock','123 main st', "1324655555","drew@mymail.com")

#print(p1.birthdate)



