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


class BankAccount: # Class must be in lower case, the actaul class will be captialzied 
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
account_list = []   # Variable shouldn't be captialized 
chase_bank = BankAccount("12345","JP Morgan Chase","1000") # Variable shouldn't be captialized 
bens_brewery = BankAccount("12346","Ben's Brewery","2000") # Variable shouldn't be captialized 

# account_list.append(constructor)
# account_list.append(Bens_Brewery)

print(chase_bank.Deposit(400))


for account in account_list:
    print(account.__dict__) 

# print(constructor.Bankfees())
    
