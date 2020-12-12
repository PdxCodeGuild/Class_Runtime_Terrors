
#computer picks 6 random numbers 1-99
import random 

def ticket():
    i = 0 
    ticket = []#
    while i < 6:
        ticket.append(random.randint(1,99))
        i += 1
    return ticket 

winning_ticket = ticket()
print(f'winning number {winning_ticket}')
#keep a running total of ticket costs and payout 

#def accounting(pay, costs):
    

payout = 0 
tic = 0 
while tic < 100000:
    
    new_ticket = ticket()
    #print(f'new ticket {new_ticket}')
    i = 0
    pay = 0
    payout -= 2
    while i < 6:
        if new_ticket[i] == winning_ticket[i]:
            pay = pay + 1
            #print(pay)
        i += 1
    #print(pay)
    if pay == 1:
        payout += 4
    elif pay == 2:
        payout += 7
    elif pay == 3:
        payout += 100
    elif pay == 4:
        payout += 50000
    elif pay == 5:
        payout += 1000000
    elif pay == 6:
        payout += 25000000       

    tic += 1

#def account(cost, payout):
 #accumulated winnings   
print(payout)   
  









