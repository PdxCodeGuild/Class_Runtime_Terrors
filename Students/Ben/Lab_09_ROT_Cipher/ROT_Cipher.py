# 10/23/2020 

ROT13 ="abcdefghijklmnopqrstuvwxyz"

# user_input = input("Enter your message here: ")

    # print(letter)
    # letter_index = user_input.index(letter)
    # print(user_input[letter_index])

def encryption_v1 ():
    user_input = input("Enter your message here: ")
    for letter in user_input:
        original_index = ROT13.index(letter)
        new_index = ( original_index + 13 ) % 26
        print(ROT13[new_index])

encryption_v1()