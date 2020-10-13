

import string
import random


def rotn(text, n):
    alphabet = string.ascii_lowercase
    output = ''
    for char in text:
        output += alphabet[(alphabet.index(char)+n)%len(alphabet)]
    return output

# print(rotn('hello', 13))


class Encryptor:
    def __init__(self):
        pass
    
    def encrypt(self, text):
        pass
    
    def decrypt(self, text):
        pass


class RotN(Encryptor):
    def __init__(self, n):
        super().__init__()
        self.n = n
    
    def encrypt(self, text):
        alphabet = string.ascii_lowercase
        output = ''
        for char in text:
            if char in alphabet:
                output += alphabet[(alphabet.index(char)+self.n)%len(alphabet)]
            else:
                output += char
        return output
    
    def decrypt(self, text):
        alphabet = string.ascii_lowercase
        output = ''
        for char in text:
            if char in alphabet:
                output += alphabet[(alphabet.index(char)-self.n)%len(alphabet)]
            else:
                output += char
        return output






class SubstitutionCipher(Encryptor):
    def __init__(self):
        alphabet = string.ascii_lowercase
        alphabet_scrambled = list(alphabet)
        random.shuffle(alphabet_scrambled)
        self.encrypt_dict = {}
        self.decrypt_dict = {}
        for i in range(len(alphabet)):
            self.encrypt_dict[alphabet[i]] = alphabet_scrambled[i]
            self.decrypt_dict[alphabet_scrambled[i]] = alphabet[i]

    
    def encrypt(self, text):
        output = ''
        for char in text:
            if char in self.encrypt_dict:
                output += self.encrypt_dict[char]
            else:
                output += char
        return output
    
    def decrypt(self, text):
        output = ''
        # for char in text:
        #     for key in self.encrypt_dict:
        #         if char == self.encrypt_dict[key]
        #             output += key
        #             break
        # for char in text:
        #     for key, value in self.encrypt_dict.items():
        #         if char == value:
        #             output += key
        #             break
        for char in text:
            if char in self.decrypt_dict:
                output += self.decrypt_dict[char]
            else:
                output += char
        return output



def encrypt_file(path, encryptor):
    with open(path, 'r') as file:
        text = file.read()
    
    text = encryptor.encrypt(text)

    with open(path, 'w') as file:
        file.write(text)

def decrypt_file(path, encryptor):
    with open(path, 'r') as file:
        text = file.read()
    
    text = encryptor.decrypt(text)

    with open(path, 'w') as file:
        file.write(text)


# encryptor = RotN(13)
# encrypt_file('odyssey.txt', encryptor)
# decrypt_file('odyssey.txt', encryptor)


encryptor = SubstitutionCipher()
encrypt_file('odyssey.txt', encryptor)

with open('odyssey.txt', 'r') as file:
    print(file.read()[:500])

decrypt_file('odyssey.txt', encryptor)


# encryptor = RotN(13)
# print(encryptor.encrypt('hello'))
# print(encryptor.decrypt('uryyb'))


# encryptor = SubstitutionCipher()
# text = 'hello'
# print(text)
# text = encryptor.encrypt(text)
# print(text)
# text = encryptor.decrypt(text)
# print(text)
