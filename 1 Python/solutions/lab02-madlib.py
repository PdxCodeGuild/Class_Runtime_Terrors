
# get words from the user
adjective = input('enter an adjective: ')
noun = input('enter a noun: ')
verb = input('enter a past-tense verb: ')

# have the user enter in multiple words, split them up
# words = input('enter an adjective, noun, and past-tense verb, separated by commas: ')
# words = words.split(',')
# print(words)

# assign the elements of the list to individual variables
# adjective = words[0]
# noun = words[1]
# verb = words[2]

# another way of assigning the elements of a list to variables
# adjective, noun, verb = words


# madlib = 'the ' + adjective + ' person ' + verb + ' the ' + noun
# madlib = f'the {words[0]} person {words[2]} the {words[1]}'
madlib = f'the {adjective} person {verb} the {noun}'

print(madlib)

