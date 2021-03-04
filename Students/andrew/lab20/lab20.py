import random
def your_ticket():
    num = 6
    ticket_list = []
    while num >= 1:
        x = random.randint(0,100000000)
        random.seed(x)
        pick = random.randint(1,99)
        ticket_list.append(pick)
        num = num - 1
    return ticket_list

def pick_six():
    num = 6
    pick_list = []
    while num >= 1:
        x = random.randint(0,100000000)
        random.seed(x)
        pick = random.randint(1,99)
        pick_list.append(pick)
        num = num - 1
    return pick_list

def pick_counter_and_checker():
    count = 1
    while count != 0:
        pick_six()
        count = count -1

def pick_validator(ticket):
    pass


#ticket = ticket()
def jackpot():
    match_count = 0
    count = 0
    winning = []
    ticket = []
    your_ticket() 
    # winning = pick_six()
    ticket = your_ticket()
    while count < 10:
        win_checker(ticket)


    # take in 100k random winning numbers
    # check the number of matches for each winning number list
    # calculate winnings based on matches and store the sum total
def win_checker(tic):
    match_count = 0
    money_spent = 0
    num = 0
    plays = 10
    ticket = []
    ticket = tic
    while plays > 0:
        winning = pick_six()
        plays -= 1
        while num < 6:
            if winning[num] == ticket[num]:
                print(f'Yes winning,{winning[num]}: your ticket {ticket[num]}')
                num += 1
                match_count += 1
               

            elif winning[num] != ticket[num]:
                print(f'no winning,{winning[num]}: your ticket {ticket[num]}')
                num += 1
                
                
        
            print(match_count)
            plays -= 1
            money_spent += 2
    print(f'money spent = {money_spent}')


# jackpot()
win_checker(your_ticket())