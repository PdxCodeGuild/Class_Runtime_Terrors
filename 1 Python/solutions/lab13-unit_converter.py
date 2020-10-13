

# dictionary method
# alternative_spellings  = {
#     'ft': ['ft', 'feet', 'foot'],
#     'mi': ['mi', 'mile', 'miles'],
#     'm': ['m', 'meter', 'meters'],
#     'km': ['km', 'kilometer', 'kilometers'],
#     'yd': ['yd', 'yard', 'yards'],
#     'in': ['in', 'inch', 'inches']
# }
# def validate_units(user_units):
#     for verified_units in alternative_spellings:
#         if user_units in alternative_spellings[verified_units]:
#             return verified_units
#     return None
# print(validate_units('feet')) # ft
# print(validate_units('kilometers')) # km





alternative_spellings  = [
    ['ft', 'feet', 'foot'],
    ['mi', 'mile', 'miles'],
    ['m', 'meter', 'meters'],
    ['km', 'kilometer', 'kilometers'],
    ['yd', 'yard', 'yards'],
    ['in', 'inch', 'inches']
]

def validate_units(user_units):
    for units_list in alternative_spellings:
        if user_units in units_list:
            return units_list[0]
    return None
# print(validate_units('feet')) # ft
# print(validate_units('kilometers')) # km



conversions = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}
# input_distance = float(input('What is the distance? '))
# input_unit = input('What are the input units? ' + '(' + ', '.join(conversions.keys()) + ') ')
# output_unit = input('What are the output units? ' + '(' + ', '.join(conversions.keys()) + ') ')
# output_distance = input_distance * conversions[input_unit] / conversions[output_unit]
# print(f'{input_distance} {input_unit} is {output_distance} {output_unit}')



# conversions = [
#     [1, 0.1, 0.001, 0.000001, 0.039370078740157, 0.0032808398950131, 0.0010936132983377, 0.00000062137119223733, 0.00000053995680345572],
#     [10, 1, 0.01, 0.00001, 0.39370078740157, 0.032808398950131, 0.010936132983377, 0.0000062137119223733, 0.0000053995680345572],
#     [1000, 100, 1, 0.001, 39.370078740157, 3.2808398950131, 1.0936132983377, 0.00062137119223733, 0.00053995680345572],
#     [1000000, 100000, 1000, 1, 39370.078740157, 3280.8398950131, 1093.6132983377, 0.62137119223733, 0.53995680345572],
#     [25.4, 2.54, 0.0254, 0.0000254, 1, 0.083333333333333, 0.027777777777778, 0.000015782828282828, 0.000013714902807775],
#     [304.8, 30.48, 0.3048, 0.0003048, 12, 1, 0.33333333333333, 0.00018939393939394, 0.0001645788336933],
#     [914.4, 91.44, 0.9144, 0.0009144, 36, 3, 1, 0.00056818181818182, 0.00049373650107991],
#     [1609344, 160934.4, 1609.344, 1.609344, 63360, 5280, 1760, 1, 0.86897624190065],
#     [1852000, 185200, 1852, 1.852, 72913.385826772, 6076.1154855643, 2025.3718285214, 1.1507794480235, 1],
# ]
# #              0                   1               2
# units = ['millimeter (mm)', 'centimeter (cm)', 'meter (m)', 'kilometer (km)', 'inch (in)', 'foot / feet (ft)', 'yard (yd)', 'mile (mi)', 'nautical mile (nmi)']


while True:
    expression = input('what is the expression? ').split()
    input_distance = float(expression[0])
    input_units = validate_units(expression[1])
    if len(expression) < 4:
        output_units = validate_units(expression[2])
    else:
        output_units = validate_units(expression[3])
    if input_units is None or output_units is None:
        print('invalid units')
        continue
    output_distance = input_distance * conversions[input_units] / conversions[output_units]
    output_distance = round(output_distance, 4)
    print(f'{input_distance} {input_units} is {output_distance} {output_units}')
    if input('would you like to do another conversion? y/n ') == 'n':
        break









