# PDX Fullstack Practice: Five More Practice

import re

# Problem 1: validate email addresses
emailCheck = re.compile(r'(.*)\@(.*)\.com')
#mo = emailCheck.search('test@gmail.com')
#mo = emailCheck.search('abc123@gmail.com')
#mo = emailCheck.search('test')
#mo = emailCheck.search('test@gmail')
#mo = emailCheck.search('test@gmail@com')
# if mo:
#     print('True')
# else:
#     print('False')

# Problem 2: validate a phone number
phoneCheck = re.compile(r'(\d){10}|(\d){3}-(\d){3}-(\d){4}|\((\d){3}\)(\s)(\d){3}-(\d){4}')
#mo = phoneCheck.search('0123456789') # True
#mo = phoneCheck.search('012-345-6789') # True
#mo = phoneCheck.search('(012) 345-6789') # True
#mo = phoneCheck.search('012-3A5-6789') # False
# mo = phoneCheck.search('1-1-1') # False
# if mo:
#     print('True')
# else:
#     print('False')

# Problem 3: clean a phone number
phoneCheck = re.compile(r'(\d){10}|(\d){3}-(\d){3}-(\d){4}|\((\d){3}\)(\s)(\d){3}-(\d){4}')
#mo = phoneCheck.search('0123456789') # 0123456789
#mo = phoneCheck.search('012-345-6789') # 0123456789
#mo = phoneCheck.search('(012) 345-6789') # 0123456789
#mo = phoneCheck.search('012-3A5-6789') # None
# mo = phoneCheck.search('1-1-1') # None
# if mo:
#     momo = mo.group()
#     nomo = ''
#     for i in range(len(str(momo))):
#         if momo[i].isdecimal():
#             nomo = nomo + momo[i]
#     print(nomo)
# else:
#     print('None')

# Problem 4: Find All Numbers
#findNum = re.compile(r'(\-)?(\d)*\.(\d)*')
findNum = re.compile(r'\-?\d\.\d\d\d?')
text = '''
name    favorite number
joe     1.23
jane    5.45
julie   -1.34
bob     4.123
'''
mo = findNum.findall(text)
print(mo)

# vowelRegex = re.compile(r'[^aeiouAEIOU]')
# print(vowelRegex.findall("RoboCop eats baby food. BABY FOOD."))