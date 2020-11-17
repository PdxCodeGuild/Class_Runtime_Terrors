

import string
import random

def scramble_letters(text):
    words = text.split()
    # words = [word.strip(string.punctuation) for word in words]
    for i in range(len(words)):
        word = words[i]
        if len(word) <= 3:
            continue
        starting_index = 0
        ending_index = len(word) - 1
        while word[starting_index] not in string.ascii_letters:
            starting_index += 1
        while word[ending_index] not in string.ascii_letters:
            ending_index -= 1
        starting_index += 1
        ending_index -= 1
        center = word[starting_index:ending_index+1]
        center = list(center)
        random.shuffle(center)
        center = ''.join(center)
        words[i] = word[:starting_index] + center + word[ending_index+1:]
    return ' '.join(words)


print(scramble_letters('The person went to the store, and bought a canoe... This doesn\'t work.'))




