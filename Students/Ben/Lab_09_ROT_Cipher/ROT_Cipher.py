# 10/23/2020 
import string
ROT13 ="abcdefghijklmnopqrstuvwxyz"


# def encryption_v1 ():
#     user_input = input("Enter your message here: ")
#     encrypted_input = ''
#     for letter in user_input:
#         original_index = ROT13.index(letter)
#         new_index = ( original_index + 13 ) % 26
#         new_letter = ROT13[new_index]
#         encrypted_input += new_letter
#     print(encrypted_input)

# encryption_v1()

def create_new_string ():
    encrypted_list = []
    new_string = ''
    rotation = input('Enter the amount of rotation to be used in the encryption: ')
    for letter in ROT13:
        original_index = ROT13.index(letter)
        new_index = (original_index + int(rotation)) % 26
        encrypted_list.insert(new_index,letter)
    new_string = ''.join(encrypted_list)
    return(new_string)

print(create_new_string())