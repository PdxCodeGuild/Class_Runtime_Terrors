#version1
user = input('enter string of characters: ')

dictionary ={'a':'n',
            'b':'o',
            'c':'p',
            'd':'q',
            'e':'r',
            'f':'s',
            'g':'t',
            'h':'u',
            'i':'v',
            'j':'w',
            'k':'x',
            'l':'y',
            'm':'z',
            'n':'a',
            'o':'b',
            'p':'c',
            'q':'d',
            'r':'e',
            's':'f',
            't':'g',
            'u':'h',
            'v':'i',
            'w':'j',
            'x':'k',
            'y':'l',
            'z':'m'
}
new = []

for letters in user:
    message = dictionary.get(letters)
    new.append(message)

message = ''.join(new)
print(message)

#version2
user1 = int(input('Rotation amount? '))
user2 = input('enter string of characters: ')


dictionary ={'a':1,
            'b':2,
            'c':3,
            'd':4,
            'e':5,
            'f':6,
            'g':7,
            'h':8,
            'i':9,
            'j':10,
            'k':11,
            'l':12,
            'm':13,
            'n':14,
            'o':15,
            'p':16,
            'q':17,
            'r':18,
            's':19,
            't':20,
            'u':21,
            'v':22,
            'w':23,
            'x':24,
            'y':25,
            'z':26
}
new = []
#need to get the value of the user2, add it it to user1, and return that key as a letter

for letters in user2:
    message = dictionary.get(letters)
    message = int(message)
    adds= message + user1
    keys = list(dictionary.keys())
    vals = list(dictionary.values())
    final = (keys[vals.index(adds)])
    new.append(final)
    
print (''.join(new))
