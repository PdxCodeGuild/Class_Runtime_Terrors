data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9] # length is 21

peak_location = 0
peak_value = 0
data_length = len(data)

def peak (data, data_length):
    peaks = {}
    x = 0
    while x < data_length-3:
        if data[x] < data[x + 1] and data[x + 1] > data[x + 2]:
            peaks.update({x + 1 : data[x + 1]})
        x += 1
    return peaks

def valley (data):
    data_length = len(data)
    valleys = {}
    x = 0
    while x < data_length-3:
        if data[x] > data[x + 1] and data[x + 1] < data[x + 2]:
            valleys.update({x + 1 : data[x + 1]})
        x += 1
    return valleys

def print_text_results(data):
    for key in data:
        print (f'A peak was located at index location {key} with a value of {data[key]}')

# def print_graph(data, data_length):
#     for indexes in data:
#         if data[indexes] = 9:
            




#     print ('{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(, ))

def main():
    peaks = peak(data, data_length)
    valleys = valley(data)
    print_text_results(peaks)
    print_text_results(valleys)
    # print_graph(data)



main()