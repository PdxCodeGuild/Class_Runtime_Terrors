#Cleon
#OOP birthyear Lab
#10-27-2020 

import datetime

class person:
    def __init__(self, fname, lname, city, age, telephone_num, email):
        self.fname = fname
        self.lname = lname
        self.city = city
        self.age = age
        self.telephone_num = telephone_num
        self.email = email
    def birthYear(self):
        current_date = datetime.datetime.today()
        return current_date.year - self.age
        #return year_now - self.age

    
human_1 = person("John", "Jacob Jingleheimer Schmidt ", "Brooklyn ", 135, 7183486543, "heimer@gmail.com")
print(f" You are {human_1.age} years old, so you were born in {human_1.birthYear()} ")


