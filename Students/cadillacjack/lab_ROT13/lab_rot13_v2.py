from string import ascii_lowercase as low
low1 = list(low[:13])
low2 = list(low[13:])
from string import ascii_uppercase as up
up1 = list(up[:13])
up2 = list(up[13:])

encoder = {}
more_encode = {}
count = 0
for i in range(13,27):
    more_encode[i] = count
    count += 1

for i in range(13):
    encoder[i] = low1[i], low2[i], up1[i], up2[i]

message = input("What is the message you would like to encode? : ")
message = list(message)

old_index = []
which_value = []
change_value = []
for i in message:
    if i in low1:
        i = low1.index(i)
        change_value.append(i)
        which_value = 1
    elif i in low2:
        i = low2.index(i)
        change_value.append(i)
        which_value = 0
    elif i in up1:
        i = up1.index(i)
        change_value.append(i)
        which_value = 3
    elif i in up2:
        i = up2.index(i)
        change_value.append(i)
        which_value = 2
    else:
        i = i
    try:
        old_index.append(encoder[i][which_value])
    except:
        old_index.append(i)
rotate = input('''
How many degrees of rotation, from 1 - 13, would you like to use? : ''')
changed_value = []
final_value = []
for i in change_value:
    i = i + int(rotate)
    if i > 12:
        i = more_encode[i]
    changed_value.append(i)
for i in changed_value:
    if i in encoder[i][0]:
        i = encoder[i][1]
    elif i in encoder[i][1]:
        i = encoder[i][0]
    elif i in encoder[i][2]:
        i = encoder[i][3]
    elif i in encoder[i][3]:
        i = encoder[i][2]
    else:
        final_value.append(i)

    final_value.append(i)
print(final_value)
    


print("".join(old_index))