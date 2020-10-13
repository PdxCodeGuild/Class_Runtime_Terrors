
import random

def peaks(data):
    
    # output = []
    # for i in range(len(data)):
    #     if i > 0 and i < len(data)-1:
    #         if data[i+1] < data[i] and data[i-1] < data[i]:
    #             output.append(i)
    # return output

    # output = []
    # for i in range(len(data)):
    #     if i == 0 or i == len(data)-1:
    #         continue
    #     if data[i+1] < data[i] and data[i-1] < data[i]:
    #         output.append(i)
    # return output

    # output = []
    # for i in range(1, len(data)-1):
    #     if data[i+1] < data[i] and data[i-1] < data[i]:
    #         output.append(i)
    # return output

    output = []
    for i in range(1, len(data)-1):
        if data[i-1] < data[i] > data[i+1]:
            output.append(i)
    return output

def valleys(data):

    output = []
    for i in range(1, len(data)-1):
        if data[i-1] > data[i] < data[i+1]:
            output.append(i)
    return output

def peaks_and_valleys(data):
    p = peaks(data)
    v = valleys(data)
    # p.extend(v)
    p += v
    p.sort()
    return p



def print_mountains(data):
    # for num in data:
    #     print('x'*num)

    for i in range(max(data), 0, -1):
        for num in data:
            if num >= i:
                print('x', end=' ')
            else:
                print(' ', end=' ')
        print()


    # for num in data:
    #     if num >= 9:
    #         print('x', end=' ')
    #     else:
    #         print(' ', end=' ')
    # print()
    # for num in data:
    #     if num >= 8:
    #         print('x', end=' ')
    #     else:
    #         print(' ', end=' ')
    # print()
    # for num in data:
    #     if num >= 7:
    #         print('x', end=' ')
    #     else:
    #         print(' ', end=' ')

# def generate_mountain(n, min, max):
#     output = []
#     for i in range(n):
#         output.append(random.randint(min, max))
#     return output


def generate_mountain(n, min, max):
    output = []
    level = (min + max) // 2
    for i in range(n):
        level += random.randint(-2, 2)
        if level < min:
            level = min
        elif level > max:
            level = max
        output.append(level)
    return output


# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
data = generate_mountain(20, 1, 10)
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))
print_mountains(data)
