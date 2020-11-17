

import random




eyes_list = ['^', '*', '~', '-', 'o', 'O', '･', 'ー', 'x', '•', 'ಠ']
mouths_list = ['_', 'o', 'O', '.', 'ᴗ', 'ᴥ']
sides_list = [
    ['[', ']'],
    ['{', '}'],
    ['(', ')'],
    ['༼ ', ' ༽'],
    ['ʕ', 'ʔ'],
]

how_many = int(input('how many emoticons would you like? '))
# user can enter: y, yes, Y, Yes, n, no, N, No, nah
# same_eyes = input('should the emoticons have the same eyes? ').lower()


same_eyes = ''
while same_eyes != 'yes' and same_eyes != 'no':
    same_eyes = input('should the emoticons have the same eyes? (yes or no)')



i = 0
while i < how_many:
    left_eye = ''
    right_eye = ''
    # if same_eyes in ['y', 'yes', 'yeah', 'yah']:
    if same_eyes[0] == 'y':
        eyes = random.choice(eyes_list)
        left_eye = eyes
        right_eye = eyes
    else:
        left_eye = random.choice(eyes_list)
        right_eye = random.choice(eyes_list)
    mouth = random.choice(mouths_list)
    while mouth.lower() == left_eye.lower() or mouth.lower() == right_eye.lower():
        mouth = random.choice(mouths_list)
    sides = random.choice(sides_list)

    print(sides[0] + left_eye + mouth + right_eye + sides[1])

    i += 1










