#version 1

'''user_input = int(input('How many feet would you lie to convert to meters: '))

answer = user_input *.3048

print (f'{user_input} feet is equal to {answer} meters')

#version 2 and 3
dictionary = {'feet': '.3048',
              'mile' : '1609.34',
              'kilometer' : '1000',
              'yard' : '.9144',
              'inch' : '.0254'
}

unit =  input ('Enter the unit of measurement you want to convert into meters ')
question =  input(f'Enter the number of {unit}[s] you want to convert into meters ')
question = int(question)
acceptable_feet= ['ft', 'feet']
acceptable_mile= ['mi','mile', 'miles']
acceptable_kilometer= ['km', 'kilometer','kilometers']
acceptable_yard= ['yd', 'yard']
acceptable_inch= ['in', 'inch']

if unit in acceptable_feet:
    dakine = dictionary.get('feet', 'No availability found') 
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
elif unit in acceptable_yard:
    dakine = dictionary.get('yard', 'No availability found') 
    dakine = float(dakine)
    answer = dakine * question
    print (f'There are {answer} meters in a {unit}')
elif unit in acceptable_inch:
    dakine = dictionary.get('inch', 'No availability found') 
    dakine = float(dakine)
    answer = dakine * question
    print (f'There are {answer} meters in a {unit}')'''

#version 4 
dictionary = {'feet': '.3048',
              'mile' : '1609.34',
              'kilometer' : '1000',
              'yard' : '.9144',
              'inch' : '.0254'
}

distance =  input ('What is the distance : ')
distance = float(distance)
#print (type(distance))
#print (distance)
input_units = input ('What are your input units: ')
output_units = input ('What are your output units: ')
acceptable_meters= ['mt', 'meters', 'meter']
acceptable_feet= ['ft', 'feet']
acceptable_mile= ['mi','mile', 'miles']
acceptable_kilometer= ['km', 'kilometer','kilometers']
acceptable_yard= ['yd', 'yard', 'yards']
acceptable_inch= ['in', 'inch']

if input_units in acceptable_meters and output_units in acceptable_feet:
    answer = distance * .3048
    print (f'There are {answer} {input_units} in a {output_units}')
'''elif unit in acceptable_mile:
    dakine = dictionary.get('mile', 'No availability found') 
    dakine = float(dakine)
    answer = dakine * question
    print (f'There are {answer} meters in a {unit}')
elif unit in acceptable_kilometer:
    dakine = dictionary.get('kilometer', 'No availability found') 
    dakine = float(dakine)
    answer = dakine * question
    print (f'There are {answer} meters in a {unit}')
elif unit in acceptable_yard:
    dakine = dictionary.get('yard', 'No availability found') 
    dakine = float(dakine)
    answer = dakine * question
    print (f'There are {answer} meters in a {unit}')
elif unit in acceptable_inch:
    dakine = dictionary.get('inch', 'No availability found') 
    dakine = float(dakine)
    answer = dakine * question
    print (f'There are {answer} meters in a {unit}')'''
     


