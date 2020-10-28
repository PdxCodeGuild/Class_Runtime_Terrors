from random import randint

counter = 0
pick = ["first", "second", "third", "fourth", "fifth", "sixth"]
ticket = []
lottery = []
matches = 0
winnings = [0,4, 7, 100, 50000, 1000000, 25000000]
balance = 0

for i in range(6):
    lucky = input(f"Enter your {pick[counter]} pick for your ticket ")
    ticket.append(int(lucky))
    counter += 1
    lottery.append(randint(1,6))


while counter <= 6:
    counter -= 1
    if ticket[counter] == lottery[counter]:
        matches += 1   
    if counter <= 0:
        break
balance += winnings[matches]

   
print(ticket)
    
print(lottery)

print("matches", matches)

print("balance", balance)
