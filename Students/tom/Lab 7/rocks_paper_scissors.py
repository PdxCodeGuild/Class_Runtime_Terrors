# Rocks, Paper, Scissors Game
# Tom Schroeder
# 10/14/2020

import random

computer_options = ['Rock', 'Paper', 'Scissors']
play_again = 'Y'

while play_again == 'Y':
    computer_choice = random.choice(computer_options)
    player_choice = input ('\nWhat is your selection? "R" for Rock, "P" for Paper, or "S" for Scissors.\n').capitalize()
    
    while player_choice != 'R' and player_choice != 'P' and player_choice != 'S':
        player_choice = input(f'\nYou made an incorrect entry of "{player_choice}". Choose "R" for Rock, "P" for Paper, or "S" for Scissors.\n').capitalize()

    if player_choice == 'R':
        player_choice = 'Rocks'

    elif player_choice == 'P':
        player_choice = 'Paper'
    
    elif player_choice == 'S':
        player_choice = 'Scissors'

    else:
        print ('There\'s an error in the code')


    if player_choice == computer_choice:
        print (f'It\'s a tie! You and the computer both picked {player_choice}.')

    elif player_choice == 'Rocks':
        if computer_choice == 'Paper':
            print (f'You chose "{player_choice}" and the computer chose "{computer_choice}." {computer_choice} covers {player_choice}. You lose.')

        else:
            print (f'You chose "{player_choice}" and the computer chose "{computer_choice}." {player_choice} breaks {computer_choice}. You win.')

    elif player_choice == 'Paper':
        if computer_choice == 'Scissors':
            print (f'You chose "{player_choice}" and the computer chose "{computer_choice}." {computer_choice} cuts {player_choice}. You lose.')
        else:
            print (f'You chose "{player_choice}" and the computer chose "{computer_choice}." {player_choice} covers {computer_choice}. You win.')
            
    elif player_choice == 'Scissors':
        if computer_choice == 'Rocks':
            print (f'You chose "{player_choice}" and the computer chose "{computer_choice}." {computer_choice} breaks {player_choice}. You lose.')
        else:
            print (f'You chose "{player_choice}" and the computer chose "{computer_choice}." {player_choice} cuts {computer_choice}. You win.')

    play_again = input ('Would you like to play again? Y or N\n').capitalize()
    while play_again != 'Y' and play_again != 'N':
        play_again = input ('Please make the correct entry. Would you like to play again? Y or N\n').capitalize()