# PDX Fullstack Rock Paper Scissors version 1
# no re-play

import random

def main():
    wpn = ['r', 'p', 's']
    print("This is a game of rock (r) paper (p) scissors (s).")
    pchoice = input("Select your weapon: ").lower()

    if pchoice not in wpn:
        print("That item is currently probited. You have been disqualified. Goodbye.")
    cchoice = random.choice(wpn)

    if (pchoice == 'r') & (cchoice == 'r'):
        print("Draw.")
    elif (pchoice == 'r') & (cchoice == 'p'):
        print("You lose.")
    elif (pchoice == 'r') & (cchoice == 's'):
        print("You win!")
    elif (pchoice == 'p') & (cchoice == 'p'): 
        print("Draw.")
    elif (pchoice == 'p') & (cchoice == 'r'):
        print("You win!")
    elif (pchoice == 'p') & (cchoice == 's'):
        print("You lose.")
    elif (pchoice == 's') & (cchoice == 's'):
        print("Draw.")
    elif (pchoice == 's') & (cchoice == 'r'):
        print("You lose.")
    elif (pchoice == 's') & (cchoice == 'p'):
        print("You win!")



main()