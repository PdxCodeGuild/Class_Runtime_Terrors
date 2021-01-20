'''
Written by James Keicher
This is a Cadillac Jack production
Submitted 10/20/20 
'''
#Opening Statement#
print('''
Welcome to cadillac Jacks Lottery.

You will be asked to select 6 numbers between 1 and 99.

You can select how many times you
would like to play your numbers.

The amount of times you choose to
play your numbers, will determine 
how many times your numbers are 
compared to the "Winning" numbers.

Each iteration will be a new set of "Winning" 
numbers, but your numbers will remain the same.

GOOD LUCK!

''')
from random import randint
counter = 0
ticket = []
lottery = []

initiate = input("would you like to play the lottery? y/n : ")

if initiate == "y":
    def lotto_ticket():
        global counter
        pick = ["first", "second", "third", "fourth", "fifth", "sixth"]
        for i in range(6):
            lucky = input(f"Enter your {pick[counter]} pick for your ticket ")
            ticket.append(int(lucky))
            counter += 1

    def lotto_numbers():
        for i in range(6):
            lottery.append(randint(1,99))
        return lottery

    def check_win(counter,):
        matches = 0
        balance = 0
        winnings = [0, 4, 7, 100, 50000, 1000000, 25000000]
        while counter <= 7:
            counter -= 1
            if ticket[counter] == lottery[counter]:
                matches += 1   
            if counter <= 0:
                break
        balance += winnings[matches]
        return balance

    def main():
        money = 0
        spent = 0
        lotto_ticket()
        chance = input("How many times would you like to play your numbers? : ")

        for i in range(int(chance)):
            lotto_numbers()
            check_win(counter,)
            m = check_win(counter)
            money += m
            spent += 2
            lottery.clear()
        if money < 0:
            money = 0

        print(f'''
Winnings = ${money}
Losses = $`{spent}''')
        
        print(f"{money - spent / spent * 100}% is your Return On Investment (ROI)")

elif initiate == "n":
    print("Thank you for playing Cadillac Jacks Lottery\nGoodbye!")

else:
    initiate = input("Please enter 'y' for Yes, or 'n' to Exit")

main()
print(ticket)