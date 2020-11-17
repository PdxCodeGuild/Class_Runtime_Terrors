

import random


def number_to_phrase(x):
    #          0      1      2      3         4      5       6       7        8       9
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if x < 10:
        return ones[x]
    elif x < 20:
        return teens[x - 10]
    elif x < 100:
        tens_digit = x//10
        ones_digit = x%10
        if ones_digit == 0:
            return tens[tens_digit-2]
        return tens[tens_digit-2] + '-' + ones[ones_digit]
    elif x < 1000:
        hundreds_digit = x//100
        tens_digit = x//10%10
        ones_digit = x%10
        if tens_digit == 0 and ones_digit == 0:
            return f'{ones[hundreds_digit]} hundred'
        elif tens_digit == 0:
            return f'{ones[hundreds_digit]} hundred and {ones[ones_digit]}'
        elif tens_digit == 1:
            return f'{ones[hundreds_digit]} hundred and {teens[ones_digit]}'
        elif ones_digit == 0:
            return f'{ones[hundreds_digit]} hundred and {tens[tens_digit-2]}'
        return f'{ones[hundreds_digit]} hundred {tens[tens_digit-2]}-{ones[ones_digit]}'

for i in range(0, 1000):
    # x = random.randint(0, 19) # int(input('enter a number: '))
    print(i, number_to_phrase(i))




















