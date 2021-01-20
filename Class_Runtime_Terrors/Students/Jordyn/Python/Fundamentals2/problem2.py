def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
        elif char != letter:
            continue
    return count

word = input("Please type a sentence: ").lower()
letter = input("Please type a letter: ").lower()
count = count_letter(word, letter)
print(f'"{letter.upper()}" was used {count} times."')