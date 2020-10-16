
#Output from m factors
baseunit={
    "ft": 3.28084,
    "mi": 0.000621371,
    "m": 1,
    "km": 0.001,
    "yd": 1.09361,
    "in": 39.3701 }
#Input to m factors
base_to_m={
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254 }

print('\nWelcome To the Unit Converter!\nOnly ft ,mi, m, km, yd and in are the Units Supported')
#User Input Distance With Float Check
while True:
    try:
        dis = float(input('What is the distance? '))
        break
    except:
        print('Invaild Input')

#User Input Unit With Dictionary Check
while True:
    
    first_unit = input('What are the input units? ' ).lower()
    if first_unit in baseunit: # Checks for supported units
        break
    else:
        print('Invaild Input, Only ft ,mi, m, km, yd and in are Supported')

#User Output Unit With Dictionary Check
while True:
    sec_unit = input('What are the output units? ').lower()
    if sec_unit in baseunit: # Checks for supported units
        break
    else:
        print('Invaild Input, Only ft ,mi, m, km, yd and in are the Supported')

#Logic/Math For Answer without if/elif
first_num_to_m = base_to_m[first_unit] * dis # Covereting Input to m
ans = first_num_to_m * baseunit[sec_unit] # Covereting to User wanted output Unit

print(f'{dis} {first_unit} is {round(ans,2)} {sec_unit}')


