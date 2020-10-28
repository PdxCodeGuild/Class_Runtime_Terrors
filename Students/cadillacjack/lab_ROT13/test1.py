from string import ascii_lowercase as low
low1 = list(low[:13])
low2 = list(low[13:])
from string import ascii_uppercase as up
up1 = list(up[:13])
up2 = list(up[13:])


initiate = input("Do you need Encoder Ring? : ")
# if query == "y":
    # rotations = input("How rotations? : ")
encoder = {}

for i in range(13):
    encoder[i] = low1[i], low2[i], up1[i], up2[i]

message = input("Whats your message? : ")
message = list(message)

def which_index(message,):
    old_index = []
    which_value = []
    for i in message:
        if i in low1:
            i = low1.index(i)
            which_value = 1
        elif i in low2:
            i = low2.index(i)
            which_value = 0
        elif i in up1:
            i = up1.index(i)
            which_value = 3
        elif i in up2:
            i = up2.index(i)
            which_value = 2
        else:
            i = i
        try:
            old_index.append(encoder[i][which_value])
        except:
            old_index.append(i)
    return old_index

def rotated(encrypted,rotations):
    encrypted = list(encrypted)
    my_rotations = []
    for i in encrypted:
        a = i
        i = encrypted.index(i) + int(rotations)
        counter = 0
        while i > 12:
            i = i - 13
            counter += 1
        if a in up:
            counter = (counter % 2) + 2
            my_rotations.append(encoder[i][counter]) 
        elif a in low:
            counter = counter % 2
            my_rotations.append(encoder[i][counter])
        else:
            my_rotations.append(i)
    print(my_rotations)

def unrotated(encrypted,rotations):
    encrypted = list(encrypted)
    my_rotations = []
    for i in encrypted:
        a = i
        i = encrypted.index(i) - int(rotations)
        if i < 0:
            i = i + 13
        counter = 0
        while i > 12:
            i = i - 13
            counter += 1
        if a in up:
            counter = (counter % 2) + 2
            my_rotations.append(encoder[i][counter]) 
        elif a in low:
            counter = counter % 2
            my_rotations.append(encoder[i][counter])
        else:
            my_rotations.append(i)
    print(my_rotations)

def main():
    old_index = which_index(message,)
    encrypted = "".join(old_index)
    which_way = input("Enter '1' to Encode, or '2' to Decode : ")
    query = input("Would you like to choose the rotation? : ")
    if query == "y":
        rotations = input("How rotations? : ")
        if which_way == "1":
            rotated(encrypted, rotations)
        elif which_way == "2":
            rotations = 13 - int(rotations)
            unrotated(encrypted,rotations)
        else: 
            which_way = input("Enter a '1' to Encode, or a '2' to Decode : ")
    elif query == "n":
        print(encrypted)
    else:
        query = input("Enter 'y' for Yes, or 'n' for No  : ")
    
main()