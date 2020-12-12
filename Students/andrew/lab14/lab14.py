import random


balance = 0
money_spent = 0


def match(m):
    global balance
    matches = m
    if matches == 1:
        balance += 4
    if matches == 2:
        balance += 7
    if matches == 3:
        balance += 100
    if matches == 4:
        balance += 50_000
    if matches == 5:
        balance += 1_000_000
    if matches == 6:
        balance += 25_000_000


def winning_number():
    num = 6
    ticket_list = []
    while num >= 1:
        x = random.randint(0, 100000000)
        random.seed(x)
        pick = random.randint(1, 50)
        ticket_list.append(pick)
        num = num - 1
    return ticket_list


def pick_six():
    num = 6
    pick_list = []
    while num >= 1:
        x = random.randint(0, 100000000)
        random.seed(x)
        pick = random.randint(1, 50)
        pick_list.append(pick)
        num -= 1
    return pick_list


number = winning_number()


def comp():
    matches = 0
    global money_spent
    p = pick_six()
    print(f'Your Ticket: {p}')
    for i, v in enumerate(p):
        if v == number[i]:

            matches += 1
        else:

            pass
    match(matches)


def run_game(num):
    money_spent = num * 2
    while num > 0:
        comp()
        num -= 1
    print(f'Winning Number: {number}')
    print("Game finished!")
    print(f"Your total winnings are: ${balance}\nYou spent: ${money_spent}")


run_game(100)
