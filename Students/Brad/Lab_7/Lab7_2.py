

import random
picks = ['Rock', 'Paper', 'Scissors']

def main():
    game = 'Y'
    while game == 'Y':

        player = input('\n Please choose one: Rock, Paper, or Scissors: ').capitalize()
        computer = random.choice(['Rock', 'Paper', 'Scissors'])
        while player not in picks:
            print('Please spell out your answer.\n')
        
        if player == computer:
            print('You tied with the computer. Please try again.\n')
        elif player == 'Rock' and computer == 'Scissors' or player == 'Paper' and computer == 'Rock' or player =='Scissors' and computer == 'Paper':
            print('You chose ' + player + ', while the computer chose ' + computer + '. YOU WIN!!!\n')  
        else: 
            print('You chose ' + player + ', while the computer chose ' + computer + '. YOU LOSE!!!\n')

        game = input('Would you like to play a game? Y or N: ')
        game = game.capitalize()
        
    print('Thank you for playing.')
main()
