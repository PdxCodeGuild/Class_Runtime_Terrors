


class bankaccount:
    def __init__(self, number, name, balance):
        self.number = number
        self.name = name
        self.balance = balance

    def bankfees(self):#5% of balance
        fees = float(self.balance * .05)
        return (fees)

    def deposit(self):
        amount = float(input('How much are you depositing? '))
        self.balance = float((self.balance + amount) - (self.bankfees()))
        print(f'Your new balance is ${self.balance}, after ${self.bankfees()} in service fees.')

    def withdraw(self):
        amount = float(input('How much are you withdrawing? '))
        self.balance = float((self.balance - amount) - (self.bankfees()))
        print(f'Your new balance is ${self.balance}, including a ${self.bankfees()} service fee.')


    def display(self):  
        inquery = input('Would you like a statement? Yes or No?').lower()
        if inquery == 'yes':
            print(f'''Your account number is {self.number}
             Your name is {self.name}
             Your account balance is {self.balance} , 
             unless our security has been breached.''')


account_1 = bankaccount('997364', 'Ted', 1000)

account_1.deposit()
account_1.withdraw()
account_1.display()

