# ROT Cypher, Tom Schroeder, 23OCT2020

import string

user_string = input ('What message would you like to encrypt?\n')
rotation_value = input ('How much would you like to rotate the characters?\n')

while True:
    try:
        int(rotation_value)
        break
    except:
        rotation_value = input ('That\'s an invalid entry. How much would you like to rotate the characters?\n')

rotation_value = int(rotation_value)

# puts each character of the printable characters into an element in a list
original_characters = []
for char in string.printable:
    original_characters.append(char)
original_characters_len = len(original_characters)


# rotates the elements of printable characters list the requested number of indexes
cypher_characters = []
x = 0
while x < original_characters_len: # will loop for each element in the list
    z = x + rotation_value # location of the character in the original list that will be appended to new list
    # print (f'value of z before correction {z}')
    while z >= original_characters_len: # reduces element location until within the valid number of elements in the list
        z -= original_characters_len
    # print (f'value of z after correction {z}')
    cypher_characters.append(original_characters[z]) # appendeds cypher list with rotated characters
    x += 1


# places each letter of input string into an element of a list
user_string_list = []
for letters in user_string:
    user_string_list.append(letters)

# makes list of index location of each letter in the input string
user_string_index = []
for letters in user_string_list:
    x = original_characters.index(letters)
    user_string_index.append(x)

# looks up index location in rotated list of characters
cypher_string_list = []
for index in user_string_index:
    x = cypher_characters[index]
    cypher_string_list.append(x)


cypher_string = ''.join(cypher_string_list) # joins elements of list together into a string


print (f'\nYour input message of "{user_string}" after rotating {rotation_value} spaces is "{cypher_string}"')