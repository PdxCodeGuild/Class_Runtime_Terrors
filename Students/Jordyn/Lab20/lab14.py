


# ------------------------------------------------ #
#                  Use Version 2
# ------------------------------------------------ #






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

    # for index in range(-1,6):
    #     if winning[index] == ticket[index]:
    #         matches += 1
    #     else:
    #         return matches

def num_matches(winning, ticket):
    matches = 0
    index = 0
    while True:
        if winning[index] == ticket[index]:
            matches += 1
            if index != 5:
                index += 1
            elif index == 6:
                return matches
        elif winning[index] != ticket[index]:
            return matches

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

values = 0
loop = 0
winning_ticket = pick6()

best_ticket = {-2:[]}

while loop < 2:

    ticket = winning_ticket

    matching = num_matches(winning_ticket, ticket)

    ticket_value = matching_value(matching)
    values += ticket_value

    loop += 1
    # for value, of_ticket in best_ticket.items():
    #     if value < ticket_value:
    #         best_ticket = {ticket_value: ticket}
    #     break
else:
    print(values, best_ticket)
    