#10-26 Note:
# class Employee:
#   def __init__(self, first, last, pay, raise_amount):
#     self.first = first
#     self.last = last
#     self.pay = pay
#     self.raise_amount = raise_amount
#     self.email = first + “.” + last + “@gmail.com”
#   def fullname(self):
#     return self.first + ” ” + self.last
#   def apply_raise(self):
#     self.pay = int(self.pay * self.raise_amount)
#     return self.pay
# empl_1 = Employee(‘alex’, ‘d’, 50, 10)
# empl_2 = Employee(‘Bruce’, ‘wayne’, 60, 0.4)
# print(empl_1.apply_raise())
# print(empl_2.apply_raise())


class BankAccount: # Class must be in lower case
    def __init__(self, accountNumber, name, balance): # First argument always starts with self
        self.accountNumber = accountNumber
        self.name = name
        self.balance = float(balance)
    def Deposit(self,amount):
        self.balance = self.balance + amount
        return (f"You have deposit ${amount}, and your new balance is ${self.balance}")
    def Withdrawal(self,amount):
        self.balance = self.balance - amount
        return (f"You have withdrwan ${amount}, and your new balance is ${self.balance}")
    def Bankfees(self):
        fee = self.balance * 0.05 
        self.balance = self.balance - fee
        return (f"You have been charged for a fee of ${fee}, and your new balance is ${self.balance}")
Account_list = []
constructor = BankAccount("12345","Buckeye Constructor","1000")
Bens_Brewery = BankAccount("12346","Ben's Brewery","2000")

Account_list.append(constructor)
Account_list.append(Bens_Brewery)


for account in Account_list:
    print(account) 

# print(constructor.Bankfees())
    
