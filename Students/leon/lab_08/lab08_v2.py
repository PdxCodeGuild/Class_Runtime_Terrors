# PDX Fullstack Lab 08 version 1
# guess the number game infinite attempts

import random

def main():
    #compy = random.randint(1,10)
    compy = 3
    victory = False
    endgame = False
    i = 1
    while (not endgame) & (not victory):
        player = input("Guess a number between 1 and 10: ")
        player = int(player)
        if (player == compy):
            print("You win! You guessed ", i, " times.")
            victory = True
            break
        else:
            i += 1 
            end = input("Wrong. Play again? ")
            if (end == 'n'):
                endgame = True
                break
            

    if (not victory):
        print("You lose. You tried ", i, "times.")

main()
        