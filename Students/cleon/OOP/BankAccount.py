#Cleon
#OOP lab
#10-26-2020

class BankAccount:
    percentage = .05
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self):
        amount = float(input("How much do you want to deposit? "))
        self.balance += amount 
        return self.balance

    
    def withdraw(self):
        amount = float(input("How much do you want to withdraw? "))
        self.balance -= amount
        return self.withdraw
    
    def bankfees(self):
        fee = self.balance * BankAccount.percentage
        self.balance -= fee
        return self.balance
    
    def display(self):
        print(f" Your balance is: {self.balance} ")


print("Welcome to Python Bank! ")
bank_1 = BankAccount(23564,"bobby", 2000.1)   
bank_1.deposit()
bank_1.display()
bank_1.withdraw()
bank_1.display()


        

        
    

