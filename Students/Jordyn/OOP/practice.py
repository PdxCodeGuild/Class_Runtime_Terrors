import random
import json
import sys

class BankAccount():
    bankfee = 1.05
    def __init__(self, name, accountNumber, balance):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance
    def details(self): #constructor, unfortunately it doesnt make much sense to use this with how I made the program as a whole
        string = str(self.name) + " " + self.accountNumber +" "+ str(self.balance)
        return string
    def deposit(self, amount):
        self.balance = float(self.balance + amount)
        return self.balance
    def withdrawal(self, amount):
        amount *= self.bankfee
        self.balance = float(self.balance - amount)

def main():
    '''Main pipeline through which everything will run'''
    member_list = json_read()
    print("\nWelcome To NonExistant Bank.\n")

    user_type_select = user_type() #Obtains new or old member

    if user_type_select == 1: #User Login
        login_name = existing_user()
        main_2(login_name)
    elif user_type_select == 2: #New User
        member_list = new_user()
        json_dump(member_list)
        main()

def main_2(login_name):
    member_list = json_read()
    selection = user_selection(login_name)
    if selection == 1: #Deposit
        new_list = deposit(login_name)
        for index in range(len(member_list)):
            if member_list[index]['name'] == login_name:
                member_list[index].update(new_list)
                json_dump(member_list)
                main_2(login_name)

    elif selection == 2: #Withdraw
        new_list = withdraw(login_name)
        for index in range(len(member_list)):
            if member_list[index]['name'] == login_name:
                member_list[index].update(new_list)
                json_dump(member_list)
                main_2(login_name)

    elif selection == 3: #View Details
        acc_details(login_name)
    elif selection == 4: #Log Out
        main()

    print('Goodbye')
    sys.exit()

def json_dump(member_list):
    '''Exports data to member_list.txt'''
    json.dump(member_list, open("member_list.txt",'w'), indent=2) #cool formatting very nice!

def json_read():
    '''Imports data from member_list.txt'''
    read = json.load(open("member_list.txt"))
    return read

def user_type():
    '''Asks if the user is a new or returning member'''
    while True:
        try:
            user_select = int(input("""Please type:
                    1. Existing Member
                    2. New Member
                    3. Exit Application\n> """))
            if user_select not in range(1, 4):
                print("\nInvalid Selection, please select 1 or 2.\n")
                
            elif user_select in range(1, 4):
                if user_select == 3:
                    print("Have a wonderful day!")
                    sys.exit()
                break
        except ValueError:
            print("\nInvalid Selection, please select 1 or 2.\n")
            # user_type()
        except TypeError:
            print("\nInvalid Selection, please select 1 or 2.\n")
            # user_type()
    return user_select

def existing_user():
    '''Finds if a user exists by username, and logs them in... no password required'''
    member_list = json_read()
    username = input("Please type in your Username:\n> ")
    for index in range(len(member_list)):
        if member_list[index]['name'] == username:
            return username
    print("Incorrect Username")
    existing_user()

def new_user():
    '''Builds a new user profile and saves it to member_list.txt'''
    member_list = json_read()
    username = input("Please type in your name:\n> ")
    new_number = rand_accountNumber()
    new_user_creation = BankAccount(username, new_number, 0)
    new_user_creation = new_user_creation.__dict__
    member_list.append(new_user_creation)
    # print(member_list)
    return member_list

def user_selection(user):
    '''Prompts user for specific options'''
    print(f"welcome {user}")
    while True:
        try:
            selection = int(input("""Would you like to:
                    1. Deposit
                    2. Withdraw
                    3. View Account Details
                    4. Log Out\n> """))
            if selection not in range(1, 5):
                print("\nInvalid Selection, please select 1, 2, 3, or 4.\n")
            elif selection in range(1, 5):
                if selection == 4:
                    print(f"Goodbye {user}!")
                    main()
                break
        except ValueError:
            print("\nInvalid Selection, please select 1, 2, 3, or 4.\n")
        except TypeError:
            print("\nInvalid Selection, please select 1, 2, 3, or 4.\n")
    return selection

def rand_accountNumber():
    '''Creates a random number for accountNumber'''
    return_number = ''
    x = 1
    while x <= 5:
        account_number = random.randint(1, 10)
        x += 1
        return_number += str(account_number)
    return return_number
def deposit(login_name): #This looks so messy haha
    '''Grabs account based on name, and updates with deposit amount'''
    member_list = json_read()
    member_details = {}
    for index in range(len(member_list)):
        if member_list[index]['name'] == login_name:
            member_details.update(member_list[index])
    d_amount = float(input("How much would you like to Deposit today?\n> "))
    account_details = BankAccount(member_details['name'], member_details['accountNumber'], member_details['balance']) #creating class defined value
    account_details.deposit(d_amount) #using a class function
    account_details = account_details.__dict__ 
    member_details.update(account_details) #updating local dictionary with class values
    # member_list[index].update(member_details) 
    print(f"You have deposited: {d_amount}. Your new balance is: {member_details['balance']}.")
    return member_details

def withdraw(login_name):
    '''Grabs account based on name, and updates with withdrawal ammount'''
    member_list = json_read()
    member_details = {}
    for index in range(len(member_list)):
        if member_list[index]['name'] == login_name:
            member_details.update(member_list[index])
    w_amount = float(input("How much would you like to Withdraw today? Reminder that all Withdrawals have an additional 0.05% \fee attached.\n> "))
    account_details = BankAccount(member_details['name'], member_details['accountNumber'], member_details['balance']) #creating class related value
    account_details.withdrawal(w_amount) 
    account_details = account_details.__dict__ #converting to dictionary
    member_details.update(account_details) #updating local dictionary with class values
    # member_list[index].update(member_details) 
    print(f"You have withdrawn: {w_amount}. Your remaining balance is: {member_details['balance']}.")
    return member_details

def acc_details(login_name):
    '''Displays all details regarding account'''
    member_details = {}
    member_list = json_read()
    for index in range(len(member_list)):
        if member_list[index]['name'] == login_name:
            member_details.update(member_list[index])
            # print(member_details)
    print(f'''#####{member_details['name'].upper()} DETAILS#####

#Account Holder Name: {member_details['name'].capitalize()}
#Account Number     : {member_details['accountNumber']}
#Account Balance    : {member_details['balance']}

    ''')
    main_2(login_name)

main()