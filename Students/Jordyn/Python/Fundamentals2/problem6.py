import string

def camel_case(text):
    new_text = ''
    punctuation = string.punctuation
    for char in text:
        if char in punctuation:
            continue
        elif char not in punctuation:
            new_text += char
    new_text = new_text.title().replace(' ', '')
    return new_text

text = input("Type a sentence: ")
camel_text = camel_case(text)
print(camel_text)