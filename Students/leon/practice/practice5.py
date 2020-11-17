# PDX Fullstack Practice: Five More Practice
# Problem 1: Pretty Numbers
import string
import pprint

def pretty_num(num):
    x = ('{:,}'.format(num))
    return(x) 

#print(pretty_num(12345678))

# Problem 2: convert number of bytes into readable format
def pretty_bytes(num):
    # byte = 8 bits
    # kb = 1,000 bytes
    # mb = 1,000 kb
    # gb = 1,000 mb
    # check if NUM < KB
    x = 0
    if (num < 1000):
        return(f"{num} bytes")
    #KB check 
    elif (num < 1000000):
        x = num / 1000
        return f"{round(x, 2)} KB"
    #MB check
    elif (num < 1000000000):
        x = num / 1000000
        return f"{round(x, 2)} MB"
    #GB check
    elif (num < 1000000000000):
        x = num / 1000000000
        return f"{round(x, 2)} GB"
    else: 
        #TB check
        x = num / (1000000000000)
        return f"{round(x, 2)} TB"
        

# print(pretty_bytes(200))
# print(pretty_bytes(3279))   # 3.28kb
# print(pretty_bytes(1561237)) # 1.5 mb
# print(pretty_bytes(7321000000)) # 7.32 gb
# print(pretty_bytes(7321999000000))

# Problem 3: Palindromes
def check_palin(text):
    rtext = text[::-1]
    if rtext == text:
        return True
    else:
        return False


#print(check_palin('racecar')) # T
#print(check_palin('palindrome')) # F

# Problem 4: Anagram
def check_ana(txt1, txt2):
    toss = []
    moss = []
    txt1 = txt1.replace(" ", "")
    toss = list(txt1)
    toss.sort()
    txt2 = txt2.replace(" ", "")
    moss = list(txt2)
    moss.sort()
    if (moss == toss):
        return True
    else:
        return False

#print(check_ana('anagram', 'nag a ram')) #T
#print(check_ana('sheep', 'goat'))        #F

# Problem 5: Scramble
import random
def scramble(text):
    # x import random
    # x .split used to create list from string
    # scan for punct and pop to place holder that also remembers index
    # new strings 'moss1', 'moss2' takes first and last chars
    # new string 'toss1' takes remaining values
    # random method used on 'toss'
    # 'toss' inserted in 'moss' between first and last
    # any punct added back on in the correct index
    # return
    
    pot1 = [] # temp holder for text.split[0]
    pot2 = [] # temp holder for text.split[1]
    moss1 = [] # build up for new scrambled word
    toss = text.split()
    pot1 = toss[0]
    pot2 = toss[1]
    moss1 = pot1[0]
    moss1 = moss1 + pot1[-1]
    print(pot1)
    print(moss1)
    # choice = len(moss)
    # for i in range(len(moss)):
    #     x = random.randint(0, len(moss))
    #     boss.append(moss[x])
    #     moss.pop(x)

    # print(boss)
    # choice = set(1, (len(toss)-1))
    # for toss in tosses:
    #     for i in range(len(toss)):
    #         if (i == 0) or (toss[i] not in string.ascii_letters):
    #             moss.append(toss[i])
    #             i += 1
    #         elif (toss[-1]):
    #             i += 1
    #             continue
    #         else:
    #             moss.append(toss[random.choice(choice)])


print(scramble('hello world!')) # hlelo wlrod!