#Rock Paper Scissors

import random

choices = ["rock", "paper", "scissors"]

def win_lose(player_hand,computer_hand):
    if player_hand == computer_hand:
        print("You Tie!")
    elif player_hand == "rock":
        if computer_hand == "paper":
            print("Computer Wins!")
        elif computer_hand == "scissors":
            print("Player Wins!")
    elif player_hand == "paper":
        if computer_hand == "rock":
            print("Player Wins!")
        elif computer_hand == "scissors":
            print("Computer Wins!")
    elif player_hand == "scissors":
        if computer_hand == "rock":
            print("Computer Wins!")
        elif computer_hand == "paper":
            print("Player Wins!")

def play_again():
    yes_list = ["yes", "ya", "y"]
    no_list = ["no", "nah", "n"]
    replay = input("Would you like to play again? Y/N\n>").lower()
    if replay in yes_list or no_list:
        if replay in yes_list:
            return 1
        elif replay in no_list:
            return 0
    else:
        print("Sorry, that was not a supported option.")
        replay = input("Would you like to play again? Y/N\n>").lower()
        if replay in yes_list:
            return 1
        elif replay in no_list:
            return 0

computer_hand = (random.choice(choices))

print("Welcome to Rock, Paper, Scissors!\n")

while True:
    player_hand = "reset" #keeps loop from taking a previous games value
    player_hand = input("Please type in the hand of your choice!\n>").lower()
    while player_hand in choices:
        win_lose(player_hand,computer_hand)
        break
    while player_hand not in choices:
        print('Sorry, that was not a supported option. Please be sure to type in "rock", "paper", or "scissors".')
        player_hand = input("Please type in the hand of your choice!\n>").lower()
        if player_hand in choices:
            win_lose(player_hand,computer_hand)
    replay = "reset" #keeps loop from taking a previous games value
    replay = play_again()
    if replay == 1:
        continue
    elif replay == 0:
        break