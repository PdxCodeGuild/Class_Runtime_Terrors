# #### Version 1

# distance_in_feet = int(input("What is the distance in feet?: "))

# def feet_to_meter(distance_in_feet):
#     m = distance_in_feet * 0.3048
#     meter = round(m,4)
#     print(f"{distance_in_feet} ft is {meter} m")
#     return(meter)

# feet_to_meter(distance_in_feet)

#### Version 2
 
metric = {
    "m" : 1,
    "km" : 1000,
    "mi" : 1609.34,
    "feet": 0.3048,
    "yard": 0.9144,
    "inch": 0.0254
}

distance = float(input("What is the distance?: "))
unit_to_be_convert = input("What are the units? \nchoose from m, km, mi, feet, yard, inch : ")

def unit_convert(distance,unit_to_be_convert):
    m = distance * metric[unit_to_be_convert]
    # print (m)
    # print(metric[unit_to_be_convert])
    meter = round(m,4)
    print(f"{distance} {unit_to_be_convert} is {meter} m")
    return(meter)

unit_convert(distance,unit_to_be_convert)
