from string import ascii_lowercase as low
low1 = list(low[:13])
low2 = list(low[13:])
from string import ascii_uppercase as up
up1 = list(up[:13])
up2 = list(up[13:])

encoder = {}

for i in range(13):
    encoder[i] = low1[i], low2[i], up1[i], up2[i]

message = input("What is the message you would like to encode? : ")
message = list(message)

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
print("".join(old_index))