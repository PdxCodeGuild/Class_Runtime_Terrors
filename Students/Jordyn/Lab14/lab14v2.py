#pick6
"""
to-do
-generate 6 random numbers saved in order as winning list
-generate ticket with 6 numbers
-compare ticket against winning order to determine winnings and costs
-loop 100,000 times
"""

import random

def pick6():
    random_list = []
    loop = 1
    while loop <= 6:
        random_list += [random.randint(1,99)]
        # print(random_list) #list creation test
        loop += 1
    else:
        return random_list

def num_matches(winning, ticket):
    matching = 0
    index = 0
    while index <= 5:
        if winning_ticket[index] == ticket[index]:
            matching += 1
            index += 1
        elif winning_ticket[index] != ticket[index]:
            matching += 0 #If matching any number use this
            index += 1 #If Matching any number use this
            # return matching #If matching in order use this
    else:
        return matching

def matching_value(matched):
    value = -2
    if matched == 0:
        return value
    elif matched == 1:
        value += 4
        return value
    elif matched == 2:
        value += 7
        return value
    elif matched == 3:
        value += 100
        return value
    elif matched == 4:
        value += 50000
        return value
    elif matched == 5:
        value += 1000000
        return value
    elif matched == 6:
        value += 25000000
        return value

value = 0
loop = 0
loop_limit = 100000
winning_ticket = pick6()

while loop < loop_limit:
    # print(winning_ticket)
    ticket = pick6()
    # print(ticket)
    # winning_ticket = [1, 1, 1, 1, 1, 1] #testing num_matches() function
    # ticket = [1, 1, 1, 1, 1, 1] #testing num_matches() function

    matching = num_matches(winning_ticket, ticket)
    if matching == 6:
        print("JACKPOT!")
    # print(matching)
    ticket_value = matching_value(matching)
    value += ticket_value
    # print(total_value)
    loop += 1
    
else:
    roi = value / (loop_limit * 2)
    if value < 0:
        print(f"""You have lost ${value}.
        Your ROI is: {roi}""")
    elif value >= 0:
        print(f"""You have earned ${value}.
        Your ROI is: {roi}""")