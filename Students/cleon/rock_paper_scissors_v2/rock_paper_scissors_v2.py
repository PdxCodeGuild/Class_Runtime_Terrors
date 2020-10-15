'''
Cleon 

'''

import random

print(" Welcome to the best Rock, Paper, Scissors game on the planet \n") # Welcome message

play_again = "yes"
while play_again == "yes" or play_again == "y" :
    Player_1 = input(" Please enter rock, paper or scissors \n ") # user input 

    rps = ["rock" ,"paper", "scissors"] # list of options
    computer = random.choice(rps) # random option is placed into computer variable 
    
    if Player_1 == computer:
        print(f"{computer}, it's a tie! ") 
    elif Player_1 == "rock":
        if computer == "scissors ":
            print(f" {computer}, you win!")
        else:
            print(f" {computer}, you lose!")

    elif Player_1 == "paper":
        if computer == "rock ":
            print(f" {computer}, you win!")
        else:
            print(f" {computer}, you lose!")

    elif Player_1 == "scissors":
        if computer == "paper ":
            print(f" {computer}, you win!")
        else:
            print(f" {computer}, you lose!")
    
    play_again = input("Play again? yes or no: ")