

unit_to_be_convert = input("What are the units you would like to convert into meters? \n Please choose from: ft, mi, m, km...  ")
distance = float(input("What is the distance?: "))


conversions = {
    "ft" : 0.3048, 
    "mi" : 1609.34, 
    "m" : 1, 
    "km" : 1000, 
}

conversion_factor = conversions[unit_to_be_convert]
output = distance*conversion_factor
output = round(output,4)
print(f"{distance} {unit_to_be_convert} is equal to {output} meters")