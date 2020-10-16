import random
choices = ('rock','paper','scissors')

while True:

    user = input('To play, choose; rock, paper or scissors. ')
    if user not in choices:
        user = input('only pick from the three choices. ')

    comp = random.choice(choices)

    if user == comp:
        print('It is a tie!')

    elif user == 'rock':
        if comp == 'paper':
            print('you lose')
        elif comp == 'scissors':
            print('you win')

    elif user == 'paper':
        if comp == 'rock':
            print('you win')
        elif comp == 'scissors':
            print('you lose')

    elif user =='scissors':
        if comp == 'rock':
            print('you lose')
        elif comp == 'paper':
            print('you win')

    again = input('Would you like to play again? Yes or No? ').lower()

    if again == 'yes':
        user = input('Which will it be this time? ')

    elif again == 'no':
        print('Thanks for playing')
        break




