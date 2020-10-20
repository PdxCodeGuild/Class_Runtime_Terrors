import random

my_ticket = [random.randint(1, 99) for num in range(0,6)]

def create_random_ticket():
    random_ticket = []
    for nums in range(0,6):
        random_ticket.append(random.randint(1,99))
    return random_ticket


def compare_tickets(ticket, random_ticket):

    total_win = 0
    match = 0 

    for x in range(len(ticket)):
       if ticket[x] == random_ticket[x]:
         match = match + 1
    if match == 1:
        total_win = total_win + 4
    elif match == 2:
        total_win = total_win + 7
    elif match == 3:
        total_win = total_win + 100
    elif match == 4:
        total_win = total_win + 50000
    elif match == 5:
        total_win = total_win + 1000000
    elif match == 6:
        total_win = total_win + 25000000
    return total_win

def pick6():
    expenses = 0
    wins = 0
    for x in range(0,20000):
        expenses += 2
        random_ticket = create_random_ticket()
        wins = wins + compare_tickets(my_ticket, random_ticket)
    print(f" ROI: {(wins - expenses) / expenses}" )
      

pick6()