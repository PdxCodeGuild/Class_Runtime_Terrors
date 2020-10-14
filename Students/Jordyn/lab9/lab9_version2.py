conversions = {'feet':0.3048, 'meters':1, 'miles':1609.34, 'kilometers':1000}

for user_unit in conversions:
    user_unit = input("Will you be converting in 'Feet', 'Meters', 'Miles', or 'Kilometers'?\n>").lower()
    
    user_input = int(input(f"How many {user_unit} are you working with?\n>"))
    length_in_meters = conversions[user_unit] * user_input

    print(f"{length_in_meters} meters.")
    break