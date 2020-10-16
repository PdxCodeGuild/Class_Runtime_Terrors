#!/bin/python3
# Filename: lab07_1_rock_paper_scissors.py
# Course: Full Stack Developer Evening Bootcamps
# Author: Peter Chow, Student
# Assignment: Lab 7: Rock Paper Scissors - Version 1
# Date: 10/14/2020
# Version 1.0

'''
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