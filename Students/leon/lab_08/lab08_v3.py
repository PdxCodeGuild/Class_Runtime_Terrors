# PDX Fullstack Lab 08 version 1
# guess the number game infinite attempts
# add a hint to error message

import random

def main():
    compy = random.randint(1,10)
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
            if (player > compy):
                end = input("Wrong. Too high! Play again? ")
                if (end == 'n'):
                    endgame = True
                    break
            else: 
                end = input("Wrong. Too low! Play again? ")
                if (end == 'n'):
                    endgame = True
                    break

    if (not victory):
        print("You lose. You tried ", i, "times.")

main()
        