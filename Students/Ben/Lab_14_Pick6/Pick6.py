# Created on 10-19-2020, Monday
print("Welcome to the Pick 6 Game! ")
balance = float()
print(f"Your balance is : $ {balance}")
import random

winning_ticket = random.sample(range(1,99),6) # This is a list contains all winning number
print(f"The winner number is {winning_ticket}")


def pick6():  # this function is used to draw 5 random number to represnet the ticket that will be used to validate against the winning ticket
    pick = random.sample(range(1,99), 6)   # This is a list represent player's ticket
    return(pick)

def validate_match():  # this function will  count the # of match for each ticket randomly picked
    match_count = 0
    user_ticket = pick6()
    # print(user_ticket)
    for element in user_ticket:                   
        index = user_ticket.index(element)        # running check of the player's list against winner's list for both numer and index
        winning_number = winning_ticket[index]
        if element == winning_number:
            match_count += 1 
            # print(f"there is a match! {winning_number}")           
        else:
            pass  
    # print(f"# of mathces: {match_count}")   
    return(match_count)

def payoff_calc(): # This function will calculate the total cost of all tickets as well as all compensation 
    payofflist = { 
    0:0,
    1:4,
    2:7,
    3:100,
    4:50000,
    5:1000000,
    6:25000000}
    attempt = int(input("How many tickets would you like to draw: "))
    payoff = 0 
    for a in range(attempt):
        count = validate_match()
        payoff += payofflist[count]
       
    cost = attempt*2
    print(f"your final balance is ${float(payoff)}")


payoff_calc()






# number_of_ticket = 1
# while number_of_ticket in range(1,11):
#     cost += validate_match(match_count)
#     number_of_ticket += 1

# print(match_count)
# print(cost)


# payoff = {
#     1:4,
#     2:7,
#     3:100,
#     4:50000,
#     5:1000000,
#     6:25000000
# }

#testing testing 11/4