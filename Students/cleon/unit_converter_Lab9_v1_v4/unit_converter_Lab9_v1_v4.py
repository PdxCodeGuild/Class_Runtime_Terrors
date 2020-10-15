'''
Cleon 
First lab
V1-V4
'''
def convertor(num_of_unit,unit_type): # function converting users input to meters
    x = num_of_unit * unit.get(unit_type) # User's input is multiplied by ft to meters conversion rate and stored in "x"
    y = round(x,4) # rounded to nearest 4 digit
    return y # returns float




unit = {"ft" : 0.3048, "mi" : 1609.34, "m" : 1, "km" : 1000, "yard" : 0.9144, "inch": 0.0254} # dictionary holding conversion rates to meters

print("Welcome to my unit convertor \n")
    
num_of_unit = float(input("What is the distance?  ")) # cast users entry from string to float
unit_type = input("Please enter a unit. 'ft' for feet , 'mi' for mile, 'm' for meter , or 'km' for kilometer, or 'inch', or 'yard' ").lower()
unit_type_2 = input("What are the output units ")   
converted_distance =  convertor(num_of_unit,unit_type)/ unit.get(unit_type_2)




print(f'{num_of_unit} {unit_type} is {round(converted_distance,6)} {unit_type_2} ')