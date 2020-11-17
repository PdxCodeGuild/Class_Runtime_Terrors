class Banc:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def bank_fees(self,amount):
        self.balance = self.balance - (amount * .05)
        print(self.balance)
        return self.balance

    def deposit(self):
        amount = input("How much would you like to deposit? : ")
        amount = int(amount)
        self.balance = amount + self.balance
        self.balance = Banc.bank_fees(customer0, amount)
        return self.balance

    def withdraw(self):
        amount = input("How much would you like to withdraw? : ")
        amount = int(amount)
        self.balance = self.balance - amount
        self.balance = Banc.bank_fees(customer0, amount)
        return self.balance

customer0 = Banc("Cadillac Jack", 1, 5000)
customer1 = Banc("James", 2, 500)

print(Banc.withdraw(customer0))
print(customer0.__dict__)
