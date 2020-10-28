import string

low_let1 = list(string.ascii_lowercase[:13])
low_let2 = list(string.ascii_lowercase[13:])
up_let1 = list(string.ascii_uppercase[:13])
up_let2 = list(string.ascii_uppercase[13:])

encoder_ring = {}
for i in range(13):
    encoder_ring[i] = low_let1[i], low_let2[i], up_let1[i], up_let2[i]

message = input("Enter a message to encrypt : ")

message = list(message)

rotation = input("How many rotations would you like to encrypt your message with? : ")
rotation = int(rotation)

def rotate(rotation,which_key):   
    while True:
        if which_key + rotation >= 13:
            which_key = rotation // which_key
            break
        else:
            which_key = which_key + rotation
    return which_key




encrypted = []
for item in message:
    if item in low_let1:
        r = low_let1.index(item)
        i = rotate(rotation,r)
        check = encoder_ring[i][1]
        # print(check)
        encrypted.append(check)
    elif item in low_let2:
        r = low_let2.index(item)
        i = rotate(rotation,r)
        check = encoder_ring[i][0]
        # print(check)
        encrypted.append(check)
    elif item in up_let1:
        r = up_let1.index(item)
        # print (r)
        i = rotate(rotation,r)
        # print(i)
        check = encoder_ring[i][3]
        # print(check)
        encrypted.append(check)
    elif item in up_let2:
        r = up_let2.index(item)
        i = rotate(rotation,r)
        check = encoder_ring[i][2]
        # print(check)
        encrypted.append(check)
    else:
        encrypted.append(item)
    
print("".join(encrypted))