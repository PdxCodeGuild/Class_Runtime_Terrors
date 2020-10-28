#PDX Code Guild excercise OOP : exercise 2
#   a) Import datetimeb) 
#   Create a class with the following attributes:
#     name
#     last name
#     surname
#     address
#     age
#     telephone
#     email
#    Create a method that based on today’s time can return
#       the person’s age. For instance, if this person was born
#       in (1992, 3, 12) and I use this method, I should get 28 
#       as a result


from datetime import date, datetime, timedelta

class Blackbook:
    global today
    def __init__(self, name, surname, address, bday, phone):
        self.name = name
        self.surname = surname
        self.address = address
        self.bday = bday
        self.phone = phone
        self.email = self.name + '.' + self.surname + "@ymail.com"
    def age(self):
        self.bday = datetime((int(self.bday[0])), (int(self.bday[1])), (int(self.bday[2])))
        self.age = ((today.year - self.bday.year) - ((today.month, today.day) <  (self.bday.month, self.bday.day)))
        return((self.age))
    
today = datetime.now()
entry_1 = Blackbook('Bub', 'StJust', 'Yerevan', (1988, 4, 1), '555-555-5554')
print(entry_1.email)
print(entry_1.age())
