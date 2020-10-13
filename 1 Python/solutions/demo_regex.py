

import re


def input_float(text):
    # return int(input(text))

    # number = input(text)
    # try:
    #     return float(number)
    # except ValueError:
    #     return None

    # if number.isdigit():
    #     return float(number)
    # return None

    number = input(text)
    if re.match(r'^-?\d+(\.\d+)?$', number):
        return float(number)
    return None



number = input_float('what is your favorite number? ')
print(number)









