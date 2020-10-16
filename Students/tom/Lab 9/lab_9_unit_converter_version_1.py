# Version 1 of Unit Converter will convert Feet to Meters
# Tom Schroeder 10/13/2020

distance_feet = input ('\nEnter the distance in feet that you want to convert to meters: ')

distance_feet = float(distance_feet)

distance_meters = distance_feet*0.3048

print (f'\n{distance_feet} ft is equal to {distance_meters:.4f} meters.')