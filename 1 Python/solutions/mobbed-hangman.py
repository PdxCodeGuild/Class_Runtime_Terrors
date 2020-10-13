import requests
import random
import string

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\. |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
 / \. |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
./ \. |
      |
=========''']

# get a list off words off the interwebs
response = requests.get('https://raw.githubusercontent.com/PdxCodeGuild/class_mountain_goat/master/data/english.txt')

#split big string into list of words
word_list = response.text.split()

#remove words fewer than 6 characters long
for word in word_list:
    if len(word) < 6:
        word_list.remove(word)

# choose a random word
chosen_word = random.choice(word_list)

# build a list of underscores to represent length and letters of guess (prevents out-of-bounds exception)
guesses_list = []
counter_wrong_guesses = 0
for i in range(len(chosen_word)):
    guesses_list.append('_')
 

#       0 1 2 3 4 5 6 7
# word: a n a c o n d a
#       a _ a _ _ _ _ a

# for REPL
while True:
    # choose a random word
    chosen_word = random.choice(word_list)
    # print(chosen_word)

    # build a list of underscores to represent length and letters of guess (prevents out-of-bounds exception)
    guesses_list = []
    guess_answers = []
    counter_wrong_guesses = 0
    for i in range(len(chosen_word)):
        guesses_list.append('_')
    while True:
        print(hangman_pics[counter_wrong_guesses])
        print(' '.join(guesses_list))
        print(f'Previous guesses: {", ".join(guess_answers)}')
        print(f"You've had {counter_wrong_guesses} wrong guesses.")
        user_guess = input('Guess a letter or the whole word: ').lower().strip()
        if user_guess in guess_answers:
            print('You already guessed that.')
            continue
        guess_answers.append(user_guess)
        if len(user_guess) > 1:
            if user_guess == chosen_word:
                print('You win, the word was "' + chosen_word+'".')
                break
            else:
                print('That guess was incorrect.')
                counter_wrong_guesses += 1
                if counter_wrong_guesses > 9:
                    print('You lose. The word was "' + chosen_word+'".')
                    break
                continue
        if user_guess not in string.ascii_lowercase:
            print('Not valid')
            continue
        # find index of correct letter in chosen_word and replace the underscores in our guesses list with the letter at the index in chosen_word 
        if user_guess in chosen_word:
            for i in range(len(chosen_word)):
                if user_guess == chosen_word[i]:
                    guesses_list[i] = user_guess
        list_chosen_word = list(chosen_word)
        # print(list_chosen_word)
        # print(guesses_list)
        if list_chosen_word == guesses_list:
            print('You win, the word was "' + chosen_word+'".')
            break
        elif user_guess not in chosen_word:
            counter_wrong_guesses += 1
        elif counter_wrong_guesses > 9:
            print('You lose. The word was "' + chosen_word+'".')
            break
            
    # less code option below:
    # if input('Would you like to play again? y/n: ') == 'n':
    #     break
    repeat = input('Would you like to play again? y/n: ')
    if repeat == 'n':
        print('Bye, Felicia')
        break