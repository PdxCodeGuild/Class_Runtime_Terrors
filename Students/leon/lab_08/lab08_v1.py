# PDX Fullstack Lab 08 version 1
# guess the number game

import random

def main():
    compy = random.randint(1,10)
    victory = False
    i = 0
    while (i < 10) & (not victory):
        player = input("Guess a number between 1 and 10: ")
        player = int(player)
        if (player == compy):
            print("You win!")
            victory = True
            break
        else: 
            print("Wrong. Try again.")
            i += 1

    if (i == 10):
        print("You lose. Insert coin to contine. 9... 8... 7.. ")

main()
        