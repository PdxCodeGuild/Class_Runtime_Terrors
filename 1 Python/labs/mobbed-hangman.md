
# Lab: Hangman

Let's write a program to play a game of [hangman](https://en.wikipedia.org/wiki/Hangman_(game))! Hangman is a word game where a secret word is chosen, then players have to guess letters until they get the word correct or they run out of chances and lose.

## Loading the Words

We can use the `requests` library to retreive a list of words from the internet, then split it into a list of strings. Then remove any strings that have 5 characters or fewer and randomly choose a word to start the game.

```python
import requests
response = requests.get('https://raw.githubusercontent.com/PdxCodeGuild/class_mountain_goat/master/data/english.txt')
print(response.text)
```

We can also download a file of english words and place it next our `.py` file and load it like so:

```python
with open('english.txt', 'r') as file:
    text = file.read()
print(text)
```

## Playing the Game

 Show them a list of 'blanks' and ask them for a letter. If they guess a letter which is in the word, show the blanks with the letters filled in. If they guess a letter which is not in the word, tell them and subtract 1 from their remaining guesses. Allow the user 10 tries to guess the letters of the word. Keep track of the letters the user has already guessed. If they guess a letter they've guessed before, tell them and do **not** subtract 1 from their guesses. Be kind, if the user can't guess the word in the number of allotted guesses, print the word and ask them if they'd like to play again.

Feel free to customize the user interface, but provide these minimum features. Below is an example run of the program.

```
_ _ _ _ _ _ _ _ _
# of guesses remaining: 10
already guessed:

Guess a letter: a
_ a _ _ _ _ a _ _
# of guesses remaining: 10
already guessed: a

Guess a letter: a
You've already guessed that
_ a _ _ _ _ a _ _
# of guesses remaining: 10
already guessed: a

Guess a letter: k
_ a _ _ _ _ a _ _
# of guesses remaining: 9
already guessed: a, k
Guess a letter:
```

## Extra Credit 1

Allow the user to user to guess the whole word- if they enter more than one letter check if the string entered matches the secret word, and if so, they win!

## Extra Credit 2

We can use the following ASCII art to show the user how many wrong guesses they've made. Hint: use the number of incorrect guesses as an index into this list.

```python
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
```

