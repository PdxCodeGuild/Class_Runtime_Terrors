def feet_to_meters():
	measurment = { 'ft':0.3048}
	distance = input("Enter the distance in feet: ")
	meters = float(distance) * measurment['ft']
	print(f'{distance} ft is {meters}m ')
    
def unit_to_meters():
	measurment = {'ft':0.03048, 'km':1000, 'mi':1609.34}
	distance = input("Enter a distance: ")
	unit = input("Select a distance unit: ft-feet, km-kilometer or mi-mile.: \n ")
	meters = float(distance) * measurment[unit]
	print(f'{distance} {unit} is {meters}m ')

def unit_to_metersV3():
	measurment = {'ft':0.03048, 'km':1000, 'mi':1609.34}
	measurment['yd'] = 0.9144
	measurment['in'] = 0.0254
	distance = input("Enter a distance: ")
	unit = input("Select a distance unit: ft-feet, km-kilometer yd-yard, in-inch or mi-mile.: \n ")
	meters = float(distance) * measurment[unit]
	print(f'{distance} {unit} is {meters}m ')

def advanced_unit_conversion():
	measurment = {'ft':0.3048, 'km':1000, 'mi':1609.34, 'm':1}
	distance = input("Enter a distance: ")
	input_unit = input("Choose an imput unit; ft-feet, km-kilometer m-meter or mi-mile.: \n ")
	output_unit = input("Choose an output unit; ft-feet, km-kilometer m-meter or mi-mile.: \n ")
	meters = float(distance) * measurment[input_unit]
	conversion = meters / measurment[output_unit]
	print(conversion)

def unit_conversion_selector():
	sel = input("Please select a conversion tool: \n v1-version 1: \n v2-version 2: \n v3-version 3: \n v4-advanved \n")
	while sel != "n":
		converters = {'v1':feet_to_meters, 'v2':unit_to_meters, 'v3':unit_to_metersV3, 'v4':advanced_unit_conversion}
		converters[sel]()
		sel = input("Please select a conversion tool: \n v1-version 1: \n v2-version 2: \n v3-version 3: \n v4-advanved \n or n to quit ")
		if sel == "n":
			print("goodbye!")
		break

	


unit_conversion_selector()