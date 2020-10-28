from string import ascii_letters as lets

lets = list(lets)
message = input("Enter a message to decrypt : ")
rotation = input("Enter an amount to rotate by : ")
message = list(message)
print(len(lets))

new_message = []
for i in message:
    if i in lets:
        i = lets.index(i)
        new = i + int(rotation)
        if new > 51:
            new = new - 51
        elif new < 0:
            new = 51 - new
        print(new)
        new_message.append(lets[new])
    else:
        new_message.append(i)

print(new_message)

