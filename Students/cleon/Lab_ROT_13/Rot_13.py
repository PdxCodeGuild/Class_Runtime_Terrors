import string

Rot 13

def rot_13(plain_text):
    enc = ""

    for e in plain_text:

        if e.islower() == True:
            e_index = ord(e) - ord('a')

            e_shifted = (e_index + 13) % 26 + ord('a')

            e_new_new = chr(e_shifted)
            enc += e_new_new
        else:
            enc += e
    return enc

plain_text = input (" Please eneter your message: \n")


print(rot_13(plain_text))


