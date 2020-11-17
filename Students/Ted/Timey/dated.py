import datetime

class Timewarp:
    def __init__(self,first,last,address,birthday): #,phone,email
        self.first = first
        self.last = last
        self.address = address
        self.birthday = birthday #yyyy-mm-dd
        #self.phone = phone
        #self.email = email

    def age(self):
        from datetime import date
        # date_object = datetime.date.today()
        # age = date_object - self.birthday
        year = self.birthday[0]
        month = self.birthday[1]
        day = self.birthday[2]
        t1 = date(year = year,month = month,day = day)
        t2 = date.today()
        age = t2 - t1
        return age

per_1 = Timewarp('Ted','Ooghe','LEO,Earth,Sol',(1962,3,12))

#'503-333-5555','tedo@gmail.com')

print(per_1.age())