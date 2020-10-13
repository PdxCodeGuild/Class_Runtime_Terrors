
import string



# two string solution
# does not handle special characters
def rot13_v1(text):
    alphabet =           'abcdefghijklmnopqrstuvwxyz'
    # rotated_alphabet = 'nopqrstuvwxyzabcdefghijklm'
    rotated_alphabet = alphabet[13:] + alphabet[:13]
    output = ''
    for char in text:
        index = alphabet.find(char)
        output += rotated_alphabet[index]
    return output

# print(rot13_v1('hello'))


# one string solution
# does not handle special characters
def rot13_v2(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        index += 13
        index %= len(alphabet)
        output += alphabet[index]
    return output

# print(rot13_v2('hello'))

# one string solution
# take non-letter characters from input and put them directly into the output
def rotn_v1(text, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        if index != -1:
            index += n
            index %= len(alphabet)
            output += alphabet[index]
        else:
            output += char
    return output

# print(rotn_v1('hello world!', 13))
# print(rotn_v1('uryyb jbeyq!', -13))


# one string solution
# rotate on a longer alphabet
def rotn_v2(text, n):
    alphabet = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    output = ''
    for char in text:
        index = alphabet.find(char)
        index += n
        index %= len(alphabet)
        output += alphabet[index]
    return output

# print(rotn_v2('hello world!', 30))
# print(rotn_v2('LIPPSy0SVPH}', -30))


def rotn_v3(text, n):
    output = ''
    for char in text:
        index = ord(char)
        index -= ord('a')
        index += n
        index %= ord('z') - ord('a') + 1 # 26
        index += ord('a')
        # print(char, ascii_code)
        output += chr(index)
    return output

# print(rotn_v3('hello', 13))
# print(rotn_v3('uryyb', -13))

def rotn_v4(text, n):
    print([ord(char) for char in text])
    print([ord(char)-97 for char in text])
    print([ord(char)-97+n for char in text])
    print([(ord(char)-97+n)%26 for char in text])
    print([(ord(char)-97+n)%26+97 for char in text])
    print([chr((ord(char)-97+n)%26+97) for char in text])
    return ''.join([chr((ord(char)-97+n)%26+97) for char in text])

print(rotn_v4('hello', 13))