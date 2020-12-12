import string

low_let = list(string.ascii_lowercase)
up_let = list(string.ascii_uppercase)


def encrypt_low(char,):
    if char >= 14:
        char = char - 13
    else:
        char = char + 13
    coded = low_let[char]
    return coded

def encrypt_up(char,):
    if char >= 14:
        char = char - 13
    else:
        char = char + 13
    coded = up_let[char]
    return coded

def main(message,):
    work = list(message)
    worked =[]
    
    for i in work:
        if i in low_let:
            i = low_let.index(i)
            worked.append(encrypt_low(i))
        elif i in up_let:
            i = up_let.index(i)
            worked.append(encrypt_up(i))
        elif i == " ":
            worked.append(i)

    worked = "".join(worked)

    print(worked)



initiate = input('''
Would you like to encrypt a message? y/n : ''')

while initiate == "y":
    message = input('''
What is the message you would like to encrypt? : ''')
    print(message)
    main(message)
    initiate = input("Would you like to encrypt another message? y/n : ")
