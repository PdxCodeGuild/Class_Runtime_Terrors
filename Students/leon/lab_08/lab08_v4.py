# PDX Fullstack Lab 08 version 1
# guess the number game infinite attempts
# add a hint to error message
# add more definitive hint to error message

import random

def main():
    #compy = random.randint(1,10)
    compy = 3
    victory = False
    endgame = False
    i = 1
    player = ''
    prior = ''
    while (not endgame) & (not victory):
        if player: 
            prior = player
        player = input("Guess a number between 1 and 10: ")
        player = int(player)
        if (player == compy):
            print("You win! You guessed ", i, " times.")
            victory = True
            break
        else:
            i += 1 
            if not prior:
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

                
            else:
                y = abs(prior-compy)
                x = abs(player-compy) 
                if (player > compy):
                    if (y) > (x):
                        end = input("Wrong. Too high! But getting closer! Play again? ").lower()
                        if (end == 'n'):
                            endgame = True
                            break
                    else:
                        end = input("Wrong. Too high! Getting further! Play again? ").lower()
                        if (end == 'n'):
                            endgame = True
                            break
                else: 
                    if (y) > (x):
                        end = input("Wrong. Too low! But getting closer! Play again? ").lower()
                        if (end == 'n'):
                            endgame = True
                            break
                    else:
                        end = input("Wrong. Too low! Getting further! Play again? ").lower()
                        if (end == 'n'):
                            endgame = True
                            break

    if (not victory):
        print("You lose. You tried ", i, "times.")

main()
        