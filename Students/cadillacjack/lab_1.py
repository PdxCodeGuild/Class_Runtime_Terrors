convert = {
"ft": 0.03048,
"mi": 1609.34,
"m": 1.0,
"km": 1000.0}

def conversion(user_distance, user_unit):
    result = float(user_distance) * user_unit
    print(f"The units you entered are equal to {result} meters.")
    
    

def main():
    user_distance = input("Please select a distance you wish to convert: ")
    user_unit = input(
'''What is the unit you would like to convert from?
For Feet : Enter "ft"
For Miles : Enter "mi"
For Meters : Enter "m"
For Kilometers : Enter "km" :  ''')
    
    unit = convert[user_unit]




    conversion(user_distance, unit)

main()

    