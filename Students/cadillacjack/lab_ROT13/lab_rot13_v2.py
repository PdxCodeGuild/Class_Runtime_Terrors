import string

low_let = list(string.ascii_lowercase)
up_let = list(string.ascii_uppercase)
num = list(string.digits)
pun = list(string.punctuation)


def encrypt_low(char,):
    if char >= 13:
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

def encrypt_num(char,):
    if char >= 7:
        char = char - 7
    else:
        char = char +3
    coded = num[char]
    return coded

def decrypt_num(char,):
    if char <= 2:
        char = char + 7
    else:
        char = char - 3
    coded = num[char]
    return coded

def encoder_ring(message,which):
    if which == 1:
        work = list(message)
        worked =[]
            
        for i in work:
            if i in low_let:
                i = low_let.index(i)
                worked.append(encrypt_low(i))
            elif i in up_let:
                i = up_let.index(i)
                worked.append(encrypt_up(i))
            elif i in num: 
                i = num.index(i)
                worked.append(encrypt_num(i))
            elif i == " ":
                worked.append(i)

        worked = "".join(worked)

        print(worked)

    if which == 2:
        work = list(message)
        worked =[]
        
        for i in work:
            if i in low_let:
                i = low_let.index(i)
                worked.append(encrypt_low(i))
            elif i in up_let:
                i = up_let.index(i)
                worked.append(encrypt_up(i))
            elif i in num: 
                i = num.index(i)
                worked.append(decrypt_num(i))
            elif i in pun:
                worked.append(i)
            elif i == " ":
                worked.append(i)

        worked = "".join(worked)

        print(worked)


def main():
    initiate = input('''
Would you like to use Cadillac Jacks encoder ring? y/n : ''')
    while initiate == "y":
        query = input('''
Enter 1 to Encrypt a message
Enter 2 to Decrypt a message
Your selection : ''')
        if query == "1":
            message = input('''
What is the message you would like to encrypt? : ''')
            print(message)
            encoder_ring(message, 1)
            initiate = input('''
Would you like to process another message? y/n : ''')
        elif query == "2":
            message = input('''
What is the message you would like to decrypt? : ''')
            print(message)
            encoder_ring(message, 2)
            initiate = input('''
Would you like to process another message? y/n : ''')
        else:
            initiate = input('''
That was an invalid response. Do you wish to continue? y/n : ''')
            

main()