"""ROT-13 CIPHER"""
import string

def rot13():
    alpha = string.ascii_lowercase
    my_word = input("Enter a wprd to encode into ROT-13: \n").lower()
    rot_word = ''
    for i in my_word:
        rot_word += alpha[(alpha.find(i)+13)%26]
    print(f'{my_word} \n')
    print(f'{rot_word}')


def rot13_v2():
    n = 0
    alpha = string.ascii_lowercase
    my_word = input("Enter a wprd to encode into ROT-13: \n").lower()
    n = input("Enter number of rotations: \n")
    rot_word = ''
    for i in my_word:
        rot_word += alpha[(alpha.find(i)+int(n))%26]
    print(f'{my_word} \n')
    print(f'{rot_word}')


rot13_v2()



#word = input("Enter a word to encode in ROT-13: \n")
