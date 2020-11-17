import datetime


# I wouldn't round money in the real world, just to make the formatting nicer.

class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.time = datetime.datetime.today().ctime()

    def deposit(self, depo):
        msg = "Deposit Screen"
        print(f"{msg:-^30}")
        self.balance += depo
        self.balance -= self.bank_fee()
        print(f'You have deposited ${depo}. \n'
              f'Your new balance is ${round(self.balance)}')
        print(f'Transaction completed on {self.time}')

    def withdrawal(self, amount):
        msg = "Withdrawal Screen"
        print(f"{msg:-^30}")
        self.balance -= amount
        self.balance -= self.bank_fee()
        print(f'You have withdrawn ${amount} \n'
              f'Your new balance is: ${round(self.balance)}')
        print(f'Transaction completed on {self.time}')

    def display(self):
        msg = "Account Infomation"
        print(f"{msg:-^30}")
        print(f'Account Holder: {self.name}\n'
              f'Current balance: ${round(self.balance)}')

    def bank_fee(self):
        # msg = "Your fees"
        # print(f"{msg:-^30}")
        fee = 0.005
        current_balance = self.balance
        fee_charge = (current_balance * fee)
        print(f'Your 0.05% fee for this transaction is ${round(fee_charge)}')
        return fee_charge
