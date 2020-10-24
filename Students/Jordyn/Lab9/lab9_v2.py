import string

def main():
    '''Initiates the program'''
    words = input('Please type something you would like encrypted: ')
    key = int(input('Please select an offset key number for encryption: '))
    new_line = ''
    if key >= 0:
        for char in words:
            if char == ' ':
                new_line += ' '
            elif char in string.ascii_lowercase:
                current_index = get_index(char, string.ascii_lowercase)
                new_line += rotate_positive(current_index, key, string.ascii_lowercase)
            elif char in string.ascii_uppercase:
                current_index = get_index(char, string.ascii_uppercase)
                new_line += rotate_positive(current_index, key, string.ascii_uppercase)
            elif char in string.digits:
                # current_index = get_index(char, string.digits)
                # new_line += rotate_positive(current_index, key, string.digits)
                new_line += char
            elif char in string.punctuation:
                # current_index = get_index(char, string.punctuation)
                # new_line += rotate_positive(current_index, key, string.punctuation)
                new_line += char
    elif key <= -1:
        for char in words:
            if char == ' ':
                new_line += ' '
            elif char in string.ascii_lowercase:
                current_index = get_index(char, string.ascii_lowercase)
                new_line += rotate_negative(current_index, key, string.ascii_lowercase)
            elif char in string.ascii_uppercase:
                current_index = get_index(char, string.ascii_uppercase)
                new_line += rotate_negative(current_index, key, string.ascii_uppercase)
            elif char in string.digits:
                # current_index = get_index(char, string.digits)
                # new_line += rotate_negative(current_index, key, string.digits)
                new_line += char
            elif char in string.punctuation:
                # current_index = get_index(char, string.punctuation)
                # new_line += rotate_negative(current_index, key, string.punctuation)
                new_line += char
    
    print(new_line)
    again = input('Would you like to run the program again? Y/N\n> ').lower()
    y_n = ['y', 'n']
    while again not in y_n:
        again = input('Would you like to run the program again? Y/N\n> ').lower()
    if again == 'y':
        main()
    elif again == 'n':
        print('Goodbye!')

def rotate_positive(index, key, a_list):
    '''Rot for positive key'''
    len_list = len(a_list) - 1
    repeat = 0
    x = index
    while repeat < key:
        x += 1
        if x > len_list:
            x = 0
        repeat += 1
    return a_list[x]

def rotate_negative(index, key, a_list):
    '''rot for negative key'''
    len_list = len(a_list) - 1
    repeat = 0
    x = index
    while repeat < abs(key):
        x -= 1
        if x == -1:
            x = len_list
        repeat += 1
    return a_list[x]

def get_index(char, alpha_list):
    '''Finds the index of the char in the submitted text'''
    for index in range(len(alpha_list)):
        if alpha_list[index] == char:
            # print(index)
            return index

print('This is an encryption program')
main()