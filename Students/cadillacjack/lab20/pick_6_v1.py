'''
Written by James Keicher
This is a Cadillac Jack production
Submitted 10/20/20 
'''


from random import randint
counter = 0
lottery = []
ticket = []

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
    lotto_ticket()

    for i in range(100000):
        lotto_numbers()
        # print(lottery)
        check_win(counter,)
        m = check_win(counter)
        money += m - 2
        lottery.clear()
    if money < 0:
        money = 0

    print(f"Winnings = ${money}")
    print(f"{money - 200000 / 200000}% is your Return On Investment (ROI)")


main()
print(ticket)
