class Employee:
    def __init__(self, first, last, pay, raise_amount):
        self.first = first
        self.last = last
        # self.pay = pay
        # self.raise_amount = raise_amount
        # self.email = first + "." + last + "@gmail.com"
    # def fullname(self):
    #     return self.first + " " + self.last
    # def apply_raise(self):
    #     self.pay = int(self.pay * self.raise_amount)
    #     return self.pay

a_dict = {}

empl_1 = Employee('alex', 'D', 50, 10)
empl_2 = Employee('Bruce', 'Wayne', 60, 0.4)

print(empl_1.__dict__)