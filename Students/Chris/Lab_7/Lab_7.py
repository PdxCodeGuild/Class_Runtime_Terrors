"""
Lab 7: Rock Paper Scissors
Let's play rock-paper-scissors with the computer.

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:

rock vs rock (tie)
rock vs paper
rock vs scissors
paper vs rock
paper vs paper
paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors
"""


import random  
# We need to import random before we can use it

choices = ["rock", "paper", "scissors"]

while True:
   
    print("Welcome to Rock, Paper, Scissors. Type 'done' at any time to exit")

    computer = random.choice(choices)

    user = ""
    
    while user not in choices:
        user = input("Choose either 'rock', 'paper', or 'scissors'").lower()
       
        if user == "done":
            break


    if user == "done":
        break

    print ("The computer chose " + computer)

    if user == computer:
        print("Looks like a tie")

    elif user == "rock":

        
        if computer == "scissors":
            print("You win!")

        
        elif computer == "rock":
            print("Sorry, You lose.")

    
    elif user == "paper":

        
        if computer == "rock":
            print("You win!")

       
        elif computer == "scissors":
            print("Sorry, You lose.")

    
    elif user == "scissors":

        
        if computer == "paper":
            print("You win!")

        
        elif computer == "rock":
            print("Sorry, You lose.")
