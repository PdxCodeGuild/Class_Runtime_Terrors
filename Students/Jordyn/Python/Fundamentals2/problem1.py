def double_letters(word):
    word_doubled = ''
    for char in word:
        word_doubled += char + char
    return word_doubled

word = input("Please type a word: ")
word = double_letters(word)
print(word)