from Bankaccount import BankAccount

acc1 = BankAccount('John Doe', 123654, 500)
acc2 = BankAccount('Jane Doe', 789258, 367)

acc1.display()

acc1.withdrawal(239)

acc1.display()

acc2.display()

acc2.deposit(2000)

acc1.deposit(1250)

acc1.display()
