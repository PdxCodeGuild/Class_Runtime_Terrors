
"""
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type),
name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.
"""
class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountnumber
        self.name = last
        self.balance = balance

    def Deposit(self, deposit,  balance):
        return self.balance + deposit

    def Withdrawal(self, withdrawal, balance):
        # self.pay = int(self.pay * self.raise_amount)
        
        return self.balance - withdrawal

    def bankfeess(self, parameter_list):
        """
        docstring
        """
        pass
    
    def display(self, accountNumber, name, balance):
        """
        docstring
        """
        pass


empl_1 = BankAccount(152536859745, ‘smith’, 50)
empl_2 = BankAccount(125458785658, ‘wayne’, 60)
print(empl_1.balance())
print(empl_2.balance())