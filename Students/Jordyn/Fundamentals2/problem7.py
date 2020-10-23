def alternating_case(text):
    new_text = ''
    length = 0
    for char in text:
        if char == ' ':
            new_text += char
            continue
        elif char != ' ':
            length += 1
            alternating = length % 2
            if alternating > 0:
                new_text += char.upper()
            elif alternating == 0:
                new_text += char.lower()
    return new_text

text = input("Type a sentence: ")
alternating_text = alternating_case(text)
print(alternating_text)