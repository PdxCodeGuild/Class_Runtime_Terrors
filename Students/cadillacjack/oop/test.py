# customer0 = ("me", 1, 1000)
# customer1 = ("you", 2, 1000)

# customers["customer0"] = customer0
# customers["customer1"] = customer1

class Banc:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    
    def new_cust(self):
        customers = {0 : (0, 0)}
        new_name = input("Enter name : ")
        new_balance = input("How much are you starting with? : ")
        last = list(customers)[-1]
        lastly = customers[last][1]
        new_account = lastly + 1
        new = "customer" + str(lastly)
        customers[new] = new_name, new_account, new_balance
        print(customers)
        return customers

    def main(self):
        customers = Banc.new_cust
        # customers = list(customers)
        print(customers)
    
Banc.new_cust
Banc.main

