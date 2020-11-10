#!/bin/python3
# Filename: lab07_2_rock_paper_scissors.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 7: Rock Paper Scissors - Version 2
# Date: 10/15/2020
# Version 1.0

'''
After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit.

'''

from random import randint

rps = ["Rock", "Paper", "Scissors"] # create a selections

computer = rps[randint(0,2)] # assign a random from selections to computer

you = False # set player to False

while you == False:
#set you to True
    you = input("Rock, Paper, Scissors? ")
    if you == computer:
        print("You picked:", you, "and Computer picked:", computer, "...Tie!")
    elif you == "Rock":
        if computer == "Paper":
            print("You picked:", you, "and Computer picked:", computer, "...You lose!")
        else:
            print("You picked:", you, "and Computer picked:", computer, "...You Won!")
    elif you == "Paper":
        if computer == "Scissors":
            print("You picked:", you, "and Computer picked:", computer, "...You lose!")
        else:
            print("You picked:", you, "and Computer picked:", computer, "...You Won!")
    elif you == "Scissors":
        if computer == "Rock":
            print("You picked:", you, "and Computer picked:", computer, "...You lose!")
        else:
            print("You picked:", you, "and Computer picked:", computer, "...You Won!")
    else:
        print("Invalid input, try again!")
    you = False
    computer = rps[randint(0,2)]