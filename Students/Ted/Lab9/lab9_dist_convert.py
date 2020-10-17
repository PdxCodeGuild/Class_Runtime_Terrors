

#build dictionary keys are units values are the portion of meter
conv_dict = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000}

#input prompt for unit
unit = input('''Choose the unit you wish to convert to meters
feet, miles, meters, kilometers. ''')

if unit not in (conv_dict):
     input:('Choose only from listed options ')

#input prompt for distance
distance = float(input('What is the length? (Do not use fractions) '))


answer = distance * conv_dict[unit]

print(f'Your answer is {answer}')

#This is as far as I could get without some help