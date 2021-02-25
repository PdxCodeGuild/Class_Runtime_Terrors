# version 2

unit_to_be_convert_from = input("What are the units you would like to convert from? \n Please choose from: in, ft, yd, m, mi, km...  ")
distance = float(input("What is the distance?: "))
unit_to_be_convert_to = input("What are the units you would like to convert to? \n Please choose from: in, ft, yd, m, mi, km...  ")

conversions = {
    "ft" : 0.3048, 
    "mi" : 1609.34, 
    "m" : 1, 
    "km" : 1000, 
    "yd": 0.9144,
    "in": 0.0254
}

conversion_factor_from = conversions[unit_to_be_convert_from]
conversion_factor_to = conversions[unit_to_be_convert_to]

meters = distance*conversion_factor_from
output = meters/conversion_factor_to
output = round(output,4)
print(f"{distance} {unit_to_be_convert_from} is equal to {output} {unit_to_be_convert_to}")