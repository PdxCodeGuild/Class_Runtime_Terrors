import random

weapons = ['rock', 'paper', 'scissors']
choose_your_weapon = random.choice(weapons)
# 
computer = random.choice(weapons)
derrick_t = False
while derrick_t == False:
    derrick_t = input('Choose your weapon: ')
    if derrick_t == computer:
        print('Tie!')
    elif derrick_t == 'rock':
        if computer == 'paper':
            print('You lost! Paper covers rock')
        else:
            print('You win! Rock smashes scissors')
    elif derrick_t == 'paper':
        if computer == 'scissors':
            print('You lost! Scissors cuts paper')
        else:
            print('You win! Paper covers rock')
    elif derrick_t == 'scissors':
        if computer == 'rock':
            print('You lost! Rock smashes scissors.')
        else:
            print('You win! Scissors cuts paper.')
    
    derrick_t = False
    computer = random.choice(weapons)
