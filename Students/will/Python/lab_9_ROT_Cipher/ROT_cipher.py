import string

lower = list(string.ascii_lowercase)
crypto_code = ''.join(lower[-13::]) + ''.join(lower[:13:])
crypto_code = list(crypto_code)
code_dict = {}
for item in crypto_code: 
    code_dict[item] = 1
#print (code_dict)
off_set = input("please enter an integer between 1 and 26: ")
off_set = int(off_set)
counter = -(off_set)
for x in lower:
    code_dict[x] = lower[counter]
    counter += 1
code_dict[' '] = ' '

#print(code_dict)
to_be_crypt = input("please provide the string to be encrypted: ")
code = []
for char in to_be_crypt:
    if char in code_dict:  
        code.append(code_dict[char])
   
print (''.join(code))
