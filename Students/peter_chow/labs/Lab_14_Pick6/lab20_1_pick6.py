#!/bin/python3
# Filename: lab20_1_pick6.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 14: Pick6 - Version 1
# Date: 10/19/2020
# Version 1.0

'''
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. 
Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. 
If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. 
Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

Steps
Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balanceHave the computer play pick6 many times and determine net balance.


'''

import random

# Generate a list of 6 random numbers representing the winning tickets
# pick6 = []
# for x in range(6):
#     pick6.append(random.randint(1,99)) # Computer generates at random int betweek 1 and 99
# print(pick6)

# for x = []
#     cpu_numbers = [random.randint(1, 99) for num in range(0,6)]
#     print('CPU numbers: ', cpu_numbers)

def pic6():
    cpu_numbers = [random.randint(1, 99) for num in range(0,6)]
    # print('CPU numbers: ', cpu_numbers)
    return cpu_numbers

def compaire(w, t): # w = winner, t = ticket
    match = 0
    for item in range(len(w)):
        if t[item] == w[item]:  
            match =+ 1
    return match

ticket = pic6()
winning = pic6() 
result = compaire(ticket, winning)
print(result)
print('Winning: ', winning)
print('Ticket: ', ticket)

def count():
    counter = 0
    for count_down in range(1000000):
        ticket = pic6()
        winning = pic6() 
        result = compaire(ticket, winning)
        counter = result
    print(counter)

count()


        





# Start your balance at 0
balance = []

