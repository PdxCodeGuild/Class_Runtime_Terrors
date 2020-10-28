class BankAccount:
    def __init__(self, accountnumber, name, balance):
        self.accountnumber = accountnumber
        self.name = name
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
    
    def bankfees(self):
        self.bankfees = int(self.balance * 0.05)
        print (f'Your bank fees are ${self.bankfees}')
    
    def display(self):
        print (f'The account owner is {self.name}')
        print (f'Your account number is {self.accountnumber}')
        print (f'Your account balance is ${self.balance}')
        # print (f'Your bank fees are ${self.bankfees}')

account = BankAccount(12345, "Tom", 1000) # account is an object because it's assigned
account.display() # method
account.bankfees()

