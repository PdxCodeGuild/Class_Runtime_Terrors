import datetime

class Timewarp:
    def __init__(self,first,last,address,birthday,phone,email):
        self.first = first
        self.last = last
        self.address = address
        self.birthday = birthday #yyyy-mm-dd
        self.phone = phone
        self.email = email

    def age(self,datetime.date.today()):
        

today = datetime.date.today()