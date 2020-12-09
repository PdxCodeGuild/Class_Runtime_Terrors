"""
 Import datetime
b) Create a class with the following attributes:
name
last name
surname
address
age
telephone
email
Create a method that based on today’s time can return the person’s age. 
  For instance, if this person was born in (1992, 3, 12) and I use this method, I should get 28 as a result
"""


from datetime import date


class Person:
    def __init__(self, fname, lname, address, bday, tel, email):
        self.first_name = fname
        self.last_name = lname
        self.address = address
        self.birthday = date(bday[0], bday[1], bday[2])
        self.tel = tel
        self.email = email

    def getAge(self):
        age = date.today() - self.birthday
        return age.days // 365


p1 = Person("fname", "lname", "123 street", (1992, 3, 12), "555", "email@email")
print(p1.birthday, p1.getAge())