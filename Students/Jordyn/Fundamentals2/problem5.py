import string

def snake_case(text):
    new_text = ''
    punctuation = string.punctuation
    for char in text:
        if char in punctuation:
            continue
        elif char not in punctuation:
            new_text += char
    new_text = new_text.lower().replace(' ', '_')
    return new_text

text = input("Type a sentence: ")
snake_text = snake_case(text)
print(snake_text)