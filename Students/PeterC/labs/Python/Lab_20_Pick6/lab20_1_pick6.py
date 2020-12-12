#!/bin/python3
# Filename: lab20_1_pick6.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 14: Pick6 - Version 1
# Date: 10/22/2020
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

def pick6():
    chosen_numbers = random.sample(range(1,99),6)
    return chosen_numbers

def num_matches(winnings, ticket):
    wincounter = 0
    for i, value in enumerate(ticket):
        if value == winnings[i]:
            wincounter += 1
    
    if wincounter == 0:
        winnings = 0
    elif wincounter == 1:
        winnings = 4
    elif wincounter == 2:
        winnings = 7
    elif wincounter == 3:
        winnings = 100
    elif wincounter == 4:
        winnings = 50000
    elif wincounter == 5:
        winnings =  1000000
    elif wincounter == 6:
        winnings = 25000000
    return winnings

def main():
    savings_account = 0
    purchase_counter = 0
    earnings = 0
    expenses = 0

    # while purchase_counter < 1000:
    for i in range(10000):
        savings_account = savings_account - 2
        expenses = expenses + 2
        winning = pick6()
        ticket = pick6()
        prizes = num_matches(winning, ticket)
        savings_account = savings_account + prizes
        earnings = earnings + prizes
        purchase_counter +=1

    return_on_investment = 100 * (earnings - expenses)/expenses
    print(f"Your earning is ${float(savings_account)}")
    print(f"Your ROI is {float(return_on_investment)}%")

if __name__ == "__main__":
    print("\nDo you feel lucky?")
    main()