"""
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.
"""


class BankAccount:
    def __init__(self, accountNumber: int, name: str, balance: float):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, amount):
        self.balance += amount
        return self.balance

    def Withdrawal(self, amount):
        self.balance -= amount
        return self.balance

    def bankFees(self):
        self.balance = self.balance * 0.95
        return self.balance

    def display(self):
        print(self.accountNumber, self.name, self.balance)


def main():
    account = BankAccount(111, "name", 100)
    print(account.Deposit(150))
    print(account.Withdrawal(50))
    print(account.bankFees())
    account.display()


main()