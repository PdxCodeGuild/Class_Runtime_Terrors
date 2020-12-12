#PDX Code Guild excercise OOP : Bank Account version 1
# create a Class 'bank account' 

#  x  Create a Python class called BankAccount which represents a / 
#       bank account, having as attributes: accountNumber / 
#       (numeric type), name (name of the account owner as string /
#       type), balance.
#  x  Create a constructor with parameters: accountNumber, name, / 
#       balance.
#    Create a Deposit() method which manages the deposit actions.
#    Create a Withdrawal() method which manages withdrawals actions.
#    Create an bankFees() method to apply the bank fees with a /
#       percentage of 5% of the balance account.
#    Create a display() method to display account details.

class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    #@classmethod
    def deposit(self, _in):
        return self.balance + _in
    def withdraw(self, _out):
        return self.balance - _out
    def bankFees(self):
        return self.balance - (self.balance * 0.05)
    def display(self):
        return self.accountNumber, self.name, self.balance

acct_1 = BankAccount(1010, 'Leon', 150)
acct_2 = BankAccount(1101, 'Zlad', 224)
print("Beginning Balances: ")
print("\t", acct_1.display())
print("\t", acct_2.display())

acct_1.balance = acct_1.deposit(110)
acct_2.balance = acct_2.withdraw(76)
acct_1.balance = acct_1.bankFees()
acct_2.balance = acct_2.bankFees()
print("Ending Balances: ")
print("\t", acct_1.display())
print("\t", acct_2.display())
