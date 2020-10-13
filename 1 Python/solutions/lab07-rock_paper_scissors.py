

# import random

# #        0        1         2
# rps = ['rock', 'paper', 'scissors']

# # 0 beats 2
# # 1 beats 0
# # 2 beats 1

# human_choice = rps.index(input('rock, papper, or scissors? '))
# computer_choice = random.randint(0, 2)

# print('human chose ' + rps[human_choice])
# print('computer chose ' + rps[computer_choice])

# if human_choice == computer_choice:
#     print('tie')
# elif (human_choice+1)%3 == computer_choice:
#     print('human lost')
# else:
#     print('human wins')







import random
from colorama import Fore, Back, Style

human_score = 0
computer_score = 0
round = 1
rps = ['rock', 'paper', 'scissors']

while True:
    while True:
        human_choice = input('rock, paper, scissors, or quit? ').lower().strip()
        if human_choice == 'quit':
            quit()
        if human_choice in rps:
            break
        else:
            print('bad input')
    computer_choice = random.choice(rps)
    print(Fore.GREEN + f'Round {round}' + Fore.RESET)
    print(f'\thuman chose {human_choice}')
    print(f'\tcomputer chose {computer_choice}')

    if human_choice == computer_choice:
        print('\tTie!')
    elif human_choice == 'rock' and computer_choice == 'paper':
        print('computer won')
        computer_score += 1
    elif human_choice == 'rock' and computer_choice == 'scissors':
        print('human won')
        human_score += 1
    elif human_choice == 'paper' and computer_choice == 'rock':
        print('human won')
        human_score += 1
    elif human_choice == 'paper' and computer_choice == 'scissors':
        print('computer won')
        computer_score += 1
    elif human_choice == 'scissors' and computer_choice == 'rock':
        print('computer won')
        computer_score += 1
    elif human_choice == 'scissors' and computer_choice == 'paper':
        print('human won')
        human_score += 1

    print(f'human score: {human_score}, computer score: {computer_score}')
    # play_again = input('would you like to play again? (y/n) ').lower().strip()
    # if play_again == 'n':
    #     break
    round += 1





    


