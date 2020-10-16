# Started on 10/14 

import random
Play_again = 'Y'

while  Play_again == 'Y':
    L = ['Rock','Paper','Scissors']
    Computer_input = random.choice(L)   
    User_input = input('What is your choice between Rock, Paper and Scissors?: ')
    if User_input == Computer_input:
        print(f'Your choice: {User_input} vs Computer choice : {Computer_input}, Its a Tie')
    else:
        if User_input == 'Rock'and Computer_input == 'Scissors':
            print(f'Your choice: {User_input} vs Computer choice : {Computer_input}, You Win!')
        elif User_input == 'Scissors'and Computer_input == 'Paper':
            print(f'Your choice: {User_input} vs Computer choice : {Computer_input}, You Win!')
        elif User_input == 'Paper'and Computer_input == 'Rock':
            print(f'Your choice: {User_input} vs Computer choice : {Computer_input}, You Win!')
        else:
            print(f'Your choice: {User_input} vs Computer choice : {Computer_input}, You Lose!')
    Play_again = input('Do you want to play again (Y/N): ')
else:
    print('Bye!')
