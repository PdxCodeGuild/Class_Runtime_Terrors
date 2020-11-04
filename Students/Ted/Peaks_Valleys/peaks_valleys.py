import random
data = [2,3,2,3,5,7,5,8,4,5,9,6,7,6]
def peaks(data):
    peak_indexs = []

    for i in range (1, len(data)-1):
        tri_0 = data[i-1]
        tri_1 = data[i]
        tri_2 = data[i+1]
        if tri_0 < tri_1 and tri_1 >tri_2:
            peak_indexs.append(i)
    return(peak_indexs)


def valleys(data):
    valley_indexs = []

    for i in range (1, len(data)-1):
        tri_0 = data[i-1]
        tri_1 = data[i]
        tri_2 = data[i+1]
        if tri_0 > tri_1 and tri_1 < tri_2:
            valley_indexs.append(i)
    return(valley_indexs)


def peaks_and_valleys(data):
    peak_valley = valleys(data)
    peak_valley.extend(peaks(data))
    peak_valley.sort()
    return(peak_valley)

print(peaks_and_valleys(data))

for num in data:
    print('x' * num)

