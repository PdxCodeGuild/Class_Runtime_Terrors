

import string
import random
import pyperclip

# get an integer from the user
def get_integer(text, min=0, max=99999):
    while True:
        num = input(text)
        if num.isdigit():
            num = int(num)
            if num < min or num > max:
                print('that is not a valid number')
                continue
            return num
        else:
            print('that is not a valid number')


def get_yes_no(text):
    while True:
        response = input(text)
        response = response.lower().trim()
        if response in ['y', 'yes', 'yeah', 'yah', 'ok', 'okay']:
            return True
        elif response in ['n', 'no', 'nah', 'nope', 'nada']:
            return False
        else:
            print('please enter yes or no')

def random_password(n_lowercase, n_uppercase, n_digits, n_punctuation):
    password = ''
    for i in range(n_lowercase):
        password += random.choice(string.ascii_lowercase)
    for i in range(n_uppercase):
        password += random.choice(string.ascii_uppercase)
    for i in range(n_digits):
        password += random.choice(string.digits)
    for i in range(n_punctuation):
        password += random.choice(string.punctuation)
    password = list(password)
    # password_list = []
    # for char in password:
    #     password_list.append(char)
    random.shuffle(password)
    password = ''.join(password)
    return password


print('Welcome the the random password generator 5000 (tm)')


while True:
    n_lowercase = get_integer('how many lower case letters? ', 0, 100)
    n_uppercase = get_integer('how many upper case letters? ')
    n_digits = get_integer('how many digits? ')
    n_punctuation = get_integer('how many punctuation characters? ')
    password = random_password(n_lowercase, n_uppercase, n_digits, n_punctuation)
    print(password)
    pyperclip.copy(password)

    if not get_yes_no('would you like another password? '):
        break
