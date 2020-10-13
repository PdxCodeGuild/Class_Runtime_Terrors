# Problem 1: Validate an Email Address
# Write a function validate_email_address which returns True if the given string is an email address, False is it isn't.
import re

def validate_email_address(email):
    
    if re.match(r'\w+@\w+\.com', email) is None:
        return False
    else:
        return True

    #return re.match(r'\w+@\w+\.com', email) is not None


# print(validate_email_address('test@gmail.com')) # True
# print(validate_email_address('abc123@gmail.com')) # True
# print(validate_email_address('test')) # False
# print(validate_email_address('test@gmail')) # False
# print(validate_email_address('test@gmail@com')) # False

# Problem 2: Validate a Phone Number
# Write a function validate_phone_number which returns True if the given string is a phone number, False if it isn't.

def validate_phone_number(phone_number):
    if re.match(r'\(?\d{3}[\s\-)]*\d{3}[\s\-]?\d{4}', phone_number) is not None:
        return True
    else:
        return False


# print(validate_phone_number('0123456789')) # True
# print(validate_phone_number('012-345-6789')) # True
# print(validate_phone_number('(012) 345-6789')) # True
# print(validate_phone_number('012-3A5-6789')) # False
# print(validate_phone_number('1-1-1')) # False

# Problem 3: Clean a Phone Number
# Write a function clean_phone_number which returns a string containing just the numbers of a phone number if it's valid, None if it's not. Hint: use capture groups.

def clean_phone_number(phone_number):
    num_groups = re.search(r'\(?(\d{3})[\s\-)]*(\d{3})[\s\-]?(\d{4})', phone_number)
    if num_groups is not None:
        return num_groups.group(1)+num_groups.group(2)+num_groups.group(3)
    else:
        return None

# print(clean_phone_number('0123456789')) # 0123456789
# print(clean_phone_number('012-345-6789')) # 0123456789
# print(clean_phone_number('(012) 345-6789')) # 0123456789
# print(clean_phone_number('012-3A5-6789')) # None
# print(clean_phone_number('1-1-1')) # None

# Problem 4: Find All Numbers
# Write a function find_numbers which returns a list of floats found in the given string.

def find_numbers(text):
    fave_number = re.findall(r'-?\d+\.?\d+', text)
    # print(fave_number)
    return [float(s) for s in fave_number]
    # print(float_fave_number)

text = '''
name  favorite number
joe   1.23
jane  5.45
julie -1.34
bob   4.123
'''
print(find_numbers(text)) # [1.23, 5.45, -1.34, 4.123]