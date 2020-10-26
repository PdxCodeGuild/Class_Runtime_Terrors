def latest_letter(word):
    length = len(word)
    length -= 1
    word_list = []
    for char in word:
        word_list += [char.lower()]
    return word_list[length]

word = input("Please input a sentence: ")
letter = latest_letter(word)
print(f"The last letter in the sentence is: {letter}")