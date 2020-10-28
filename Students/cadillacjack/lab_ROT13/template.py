import string
low_let = list(string.ascii_lowercase)
low_let1 = list(string.ascii_lowercase[:13])
low_let2 = list(string.ascii_lowercase[13:])
up_let = list(string.ascii_uppercase)
up_let1 = list(string.ascii_uppercase[:13])
up_let2 = list(string.ascii_uppercase[13:])


key_code = {}
for i in range (1,14):
    key_code[i] = low_let1[i-1], low_let2[i-1], up_let1[i-1], up_let2[i-1]


message = input("What is the secret messgae? : ")
rotations = int(input("How many rotations would you like to use? : "))

def converter(selection):
    valued = 0
    while selection > 13:
        selection = selection - 13
        valued += 1
    if selection < 13:
        selection = selection
        valued += 1
    valued = valued%2
    return selection, valued

message= list(message)

secret_message = []

for character in message:
    if character in low_let:
        selection = (low_let.index(character) + 1)
        for i in range(rotations):
            selection, valued = converter(selection)
            character = key_code[selection][valued]
            selection = low_let.index(character) + 1
        selection, valued = converter(selection)
        secret_message.append(key_code[selection][valued])
    elif character in up_let:
        selection = up_let.index(character) + 1
        for i in range(rotations):
            selection, valued = converter(selection)
            # print(selection)
            character = key_code[selection][valued]
            # print(character)
            selection = low_let.index(character) + 1
            # print(selection)
        selection, valued = converter(selection)    
        secret_message.append(key_code[selection][valued+2])
    else:
        secret_message.append(character)
print(''.join(secret_message))