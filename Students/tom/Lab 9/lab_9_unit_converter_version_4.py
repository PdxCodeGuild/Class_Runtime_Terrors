# Version 3 of Unit Converter adds more conversion factors
# Tom Schroeder 10/14/2020

original_distance = float(input ('\nEnter the distance that you want to convert: '))

# user inputs the units of the original disance
original_units = input ('Enter the original units (ft, mi, m, km): ')

converted_units = input ('Enter the units to convert to (ft, mi, m, km): ')

converted_distance = 0

if original_units == converted_units:
    converted_distance = original_distance

elif original_units == 'ft' and converted_units == 'mi':
    converted_distance = (original_distance * 0.000189394)

elif original_units == 'ft' and converted_units == 'm':
    converted_distance = (original_distance * 0.3048)

elif original_units == 'ft' and converted_units == 'km':
    converted_distance = (original_distance * 0.0003048)

elif original_units == 'mi' and converted_units == 'ft':
    converted_distance = (original_distance * 5280)

elif original_units == 'mi' and converted_units == 'm':
    converted_distance = (original_distance * 1609.34)

elif original_units == 'mi' and converted_units == 'km':
    converted_distance = (original_distance * 1.60934)

elif original_units == 'm' and converted_units == 'ft':
    converted_distance = (original_distance * 3.28084)

elif original_units == 'm' and converted_units == 'mi':
    converted_distance = (original_distance * 0.000621371)

elif original_units == 'm' and converted_units == 'km':
    converted_distance = (original_distance * 0.000621371)

elif original_units == 'km' and converted_units == 'ft':
    converted_distance = (original_distance * 3280.84)

elif original_units == 'km' and converted_units == 'mi':
    converted_distance = (original_distance * 0.621371)

elif original_units == 'km' and converted_units == 'm':
    converted_distance = (original_distance * 1000)

else:
    print ('Units entered incorrectly. Good bye.')


if converted_distance != False:
    print (f'{original_distance} {original_units} is {converted_distance:.4f} {converted_units}' )