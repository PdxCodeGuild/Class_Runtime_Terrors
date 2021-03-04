#Cleon
#Lab 14

import random


def pick6():
    x= 0
    i = []
    while x < 6:
        i.append(random.randint(1,99))
        x += 1
    return i   

def num_matches(winning , tickets ): # checks number of matches
    i = 0
    for x,y in zip(winning, tickets): 
        if x == y :
            i +=1
    return i


def match_winnings(x): # x is num_match function
    if x == 1:
        return 4
    elif x == 2:
        return 7
    elif x == 3:
        return 100
    elif x == 4:
        return 50000
    elif x == 5:
        return 1000000
    elif x == 6:
        return 25000000
    else:
        return 0



winning_ticket = pick6()
count = 0 # number of  time played
balance = 0
#total_cost_of_tickets = 0
user_winnings = 0
while count < 1000:
    #total_cost_of_tickets +=2
    current_ticket = pick6()
    matches = num_matches(winning_ticket,current_ticket)
    user_winnings  += match_winnings(matches) #stores winning if any
    balance += user_winnings # adds winnings if any to balance 
    balance -= 2  # removes ticket cost from balance 
    count += 1
fin_b = "{:,}".format(balance) # thousands separator and return a string with commas added to number...int to str
print(f" Final balance : ${fin_b} ")
    

    





     



        
    
        





