#lab 2 
# Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then use the .split() function to store each adjective and later use it in your story.

# Add randomness! Use the random module, rather than selecting which adjective goes where in the story.



noun = input('enter a noun: ')
verb = input('enter a present-tense verb: ')
adjective = input('enter an adjective: ')


madlib = f'the {adjective} employee had to {verb} to get their {noun} back'

print(madlib)