# This whole file was just to write my functions

def to_feet(user_distance, user_unit):
    result = float(user_distance) * user_unit / convert["ft"]
    print(f"The units you entered are equal to {result} Feet.")

def to_miles(user_distance, user_unit):
    result = float(user_distance) * user_unit / convert["mi"]
    print(f"The units you entered are equal to {result} Miles.")

def to_kilometers(user_distance, user_unit):
    result = float(user_distance) * user_unit / convert["km"]
    print(f"The units you entered are equal to {result} Kilometers.")

def to_yards(user_distance, user_unit):
    result = float(user_distance) * user_unit / convert["y"]
    print(f"The units you entered are equal to {result} yards.")

def to_inches(user_distance, user_unit):
    result = float(user_distance) * user_unit / convert["i"]
    print(f"The units you entered are equal to {result} inches.")

def to_meters(user_distance, user_unit):
    result = float(user_distance) * user_unit
    print(f"The units you entered are equal to {result} meters.")