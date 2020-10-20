# Created on 10-19-2020, Monday
print("Welcome to the Pick 6 Game! ")
balance = float()
print(f"Your balance is : $ {balance}")
import random

ticket = random.sample(range(1,99),6)
print(ticket)

match_count = 0
cost = 0

def validate_match(match_count):
    pick = random.sample(range(1,99), 6)
        # print(pick)
    for element in pick:
        # print(element)
        index = pick.index(element)
        # print(index)
        winning_number = ticket[index]
        # print(winning_number)
        if element == winning_number:
            match_count += 1            
        else:
            pass  
        cost = 2*(index+1)
        # print(cost)
    print(f"Current # of mathces: {match_count}")
    return(match_count)
    return(cost)

number_of_ticket = 1
while number_of_ticket in range(1,11):
    validate_match(match_count)
    number_of_ticket += 1

print(match_count)
print(cost)


payoff = {
    1:4,
    2:7,
    3:100,
    4:50000,
    5:1000000,
    6:25000000
}

