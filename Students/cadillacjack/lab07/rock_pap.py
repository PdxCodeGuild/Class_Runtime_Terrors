import random

rps = ["rock", "paper", "scissors"]
y = 1
n = 0


play = input("Would you like to play Rock, Paper, Scissors? y/n : ")

while play == "y":
    player = input('''
Enter an "r" for Rock
Enter a "p" for Paper
Enter an "s" for Scissors : ''')
    opponent = random.choice(rps)

    if player == "r":
        player = rps[0]
    elif player == "p":
        player = rps[1]
    elif player == "s":
        player = rps[2]
    else:
        input('''
Please enter a valid input.
Enter an "r" for Rock
Enter a "p" for Paper
Enter an "s" for Scissors : ''')

    print(f'''
You have selected {player}. Your opponent has selected {opponent}.
    ''')

    if player == opponent:
        print("This match was a tie!")
    elif player == "rock" and opponent == "scissors":
        print("Congratulations, You have won the match!")
    elif player == "rock" and opponent == "paper":
        print("You have lost the match!")
    elif player == "scissors" and opponent == "paper":
        print("Congratulations, You have won the match!")
    elif player == "scissors" and opponent == "rock":
        print("You have lost the match!")
    elif player == "paper" and opponent == "rock":
        print("Congratulations, You have won the match!")
    elif player == "paper" and opponent == "scissors":
        print("You have lost the match!")

    play = input("Would you like to play again? y/n : ")



