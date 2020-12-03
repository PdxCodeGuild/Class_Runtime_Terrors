"""
ROT Cipher
"""

def rot(m, rotn=13):
    lm = []
    for l in m.lower().strip():
        lm.append(chr((ord(l) - 97 + rotn) % 26 + 97))
    return "".join(lm)

def main():
    word = input("enter a word to process: ")
    rotn = int(input("enter the amount of rotation or enter for 13: ") or "13")
    ret = rot(word,rotn)
    print(ret)

main()
# tests()