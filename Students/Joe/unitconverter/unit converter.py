#Version 1 of Converter Lab 3 
dictionary = {'1': '.3048'}

question = int (input ('Enter the number of feet you want to convert into meters '))

dakine = dictionary.get('1', 'No availability found') 
dakine = float(dakine)
print (dakine * question)

#version 2 of converter Lab 3
dictionary = {'feet': '.3048',
              'mile' : '1609.34',
              'kilometer' : '1000'
}

unit =  input ('Enter the unit of measurement you want to convert into meters ')
question =  input(f'Enter the number of {unit}s you want to convert into meters ')
question = int(question)
acceptable_feet= ['ft', 'feet']
acceptable_mile= ['mi','mile', 'miles']
acceptable_kilometer= ['km', 'kilometer','kilometers']

if unit in acceptable_feet:
    dakine = dictionary.get('feet', 'No availability found') 
    print (type(dakine))
    dakine = float(dakine)
    answer = dakine * question
    print (f'There are {answer} meters in a {unit}')
elif unit in acceptable_mile:
    dakine = dictionary.get('mile', 'No availability found') 
    dakine = float(dakine)
    answer = dakine * question
    print (f'There are {answer} meters in a {unit}')
elif unit in acceptable_kilometer:
    dakine = dictionary.get('kilometer', 'No availability found') 
    dakine = float(dakine)
    answer = dakine * question
    print (f'There are {answer} meters in a {unit}')