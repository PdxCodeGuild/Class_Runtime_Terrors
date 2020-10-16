import random


initiate = input('''
Would you like to play Guess the Number?
Enter "y" for Yes, or "n" for No :  ''')

secret = random.randint(1,10)

counter = 0

while initiate == "y":
    guess = input('''
Enter a number between 1 and 10
Your Guess : ''')
    
    if int(guess) == secret:
        print(f'''
Congratulations! You have successfully guessed the secret number!
You made {counter} attempts before successfully guessing the number. ''')
        initiate = input('''
Would You like to play again? 
Enter "y" for Yes, or "n" for No :  ''')
        counter = 0
        secret = random.randint(1,10)
    elif int(guess) != secret:
        counter += 1
        print('''
That is not the secret number. Try again...
        ''')
