

#build dictionary keys are units values are the portion of meter
conv_dict = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000}

#input prompt for unit
unit = input('''Choose the unit you wish to convert to meters
feet, miles, meters, kilometers. ''')
#input prompt for distance
distance = float(input('What is the length? (Do not use fractions) '))

if unit not in conv_dict(key): input:('Choose only from listed options ')

answer = conv_dict[unit] * distance

print(f'Your answer is {answer}')

