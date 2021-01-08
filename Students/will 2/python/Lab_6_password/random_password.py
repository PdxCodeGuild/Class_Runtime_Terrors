import string
import random

qty_lower = input( "please enter the number of lowercase letters you would like: ")
qty_lower = int(qty_lower)
qty_upper = input( "please enter the number of uppercase letters you would like: ")
qty_upper = int(qty_upper)
qty_nums = input( "please enter the number of numbers you would like: ")
qty_nums = int(qty_nums)
qty_chars = input( "please enter the number of special characters you would like: ")
qty_chars = int(qty_chars)

def gen(char,qty):
    qty_rndm_char = []
    while len(qty_rndm_char) <= qty:
        rndm_char = random.choice(char)
        qty_rndm_char.append(rndm_char)
        # psw_char = ''.join(qty_rndm_char)
    return qty_rndm_char

lower = string.ascii_lowercase
upper = string.ascii_uppercase
nums = string.digits
chars = string.punctuation

total_chars = gen(lower,qty_lower) + gen(upper,qty_upper) + gen(nums,qty_nums) + gen(chars,qty_chars)

final_password = random.sample(total_chars, len(total_chars))

password = ''.join(final_password)
print(f"your new password is {password}")
