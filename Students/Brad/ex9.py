

def main():
    while True:

        # Know information
        unit_con = {
            'ft': .3048, 
            'm': 3.28084, 
            'mi': 1609.34, 
            'km': 1000, 
            'yd': .9144, 
            'in': .0254
            }
        choices = ['ft', 'm', 'mi', 'km', 'yd', 'in']

        # input informatin required from user
        message = f'Conversion calculator. Converts between {choices}'
        print(message)
        distance = input('What is the numerical distance you would like to convert?: ')
        while distance.isalpha():
            print('please enter a numeric value.: ')
            distance = input('What is the numerical distance you would like to convert?: ')

        input_unit = input('What are the input units?: ')
        while not unit_con.get(input_unit):
            print(f'Invalid entry. Please add one of the choices. {choices}')
            input_unit = input('What are the input units?: ')


        output_unit = input('What are the output units?: ')
        while not unit_con.get(output_unit):
            print(f'Invalid entry. Please add one of the choices. {choices}')
            output_unit = input('What are the output units?: ')

        # converts all forms of units to meters
        con_type = unit_con[input_unit]
        distance = float(distance)
        to_meters = distance * con_type

        # converts meters to output unit type
        if output_unit != "m":
            new_distance = to_meters / unit_con[output_unit]
                
        # if meters is the final answer
        elif input_unit == 'm' == output_unit:
            new_distance = distance
        else:
            new_distance = to_meters

        # Output statement
        output = f'The {distance} {input_unit} converts to {new_distance:.5f} {output_unit}'
        print(output)

        new_calc = input('Would you like to convert another distance? y/n: ')

        while new_calc not in ['y','n']:
            print('Please enter a valid choice!')
            new_calc = input('Would you like to convert another distance? y/n: ')

        if new_calc == 'y':
            print('Planning on taking a trip?')
                    
        elif new_calc == 'n':
            print('So long')
            break

main()