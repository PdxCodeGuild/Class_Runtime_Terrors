# Version 2 of Unit Converter will convert a variety of units to meters
# Tom Schroeder 10/13/2020

original_distance = float(input ('\nEnter the distance in feet that you want to convert to meters: '))


# dictionary of conversion values
conversion_values = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}

# user inputs the units of the original disance
original_units = input ('Enter the original units (ft, mi, m, km): ')

# get the conversion factor from the dictionary
conversion_factor = conversion_values[original_units]

# multiply the original distance by the conversion factor
converted_distance = original_distance * conversion_factor

# print a message showing the entered distance and the converted distance
print (f'\n{original_distance} {original_units} is equal to {converted_distance:.4f} meters.')