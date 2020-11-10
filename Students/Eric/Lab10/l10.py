
def peaks(data):
    elist = [] # Empty List
    for x in range(len(data)): # Lenth of Data
        if x > 0 and x < len(data)-1: # Not First or Last Data Point
            if data[x+1] < data[x] and data[x-1] < data[x]: # Checking if New Number is bigger then the last and the next number
                elist.append(x)
    return elist

def valleys(data):
    elist = [] # Empty List
    for x in range(len(data)): # Lenth of Data
        if x > 0 and x < len(data)-1: # Not First or Last Data Point
            if data[x-1] > data[x] < data[x+1]: # Checking if the last number bigger, and the next is bigger
                elist.append(x)
    return elist

def peaks_and_valleys(data):
    pv =peaks(data) + valleys(data)
    pv.sort()
    return pv

def mountains(data):
    for x in range(max(data), 0 , -1): #Count Down for Max to Zero
        for y in data:
            if y > x:
                print('x', end=' ') # Print X without Newline
            else:
                print(' ', end=' ') #Print " " without Newline
        print() # New Line

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print('The Data is ', data)
    print('The Peaks are : ',peaks(data))
    print('The Valleys are : ', valleys(data))
    print('The Peaks and Valleyes are: ',peaks_and_valleys(data))
    mountains(data)

main()