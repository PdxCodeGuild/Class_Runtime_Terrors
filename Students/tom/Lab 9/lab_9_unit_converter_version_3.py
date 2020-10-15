# Version 3 of Unit Converter adds more conversion factors
# Tom Schroeder 10/13/2020

original_distance = float(input ('\nEnter the distance that you want to convert to meters: '))


# dictionary of conversion values
conversion_values = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

# user inputs the units of the original disance
original_units = input ('Enter the original units (in, ft, yd, mi, m, km): ')

# get the conversion factor from the dictionary
conversion_factor = conversion_values[original_units]

# multiply the original distance by the conversion factor
converted_distance = original_distance * conversion_factor

# print a message showing the entered distance and the converted distance
print (f'\n{original_distance} {original_units} is equal to {converted_distance:.4f} meters.')