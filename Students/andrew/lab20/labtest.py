import random


def pick_six():
    num = 6
    pick_list = []
    while num >= 1:
        x = random.randint(0, 100000000)
        random.seed(x)
        pick = random.randint(1, 99)
        pick_list.append(pick)
        num = num - 1
    return pick_list


def num_gen():
    s = random.randint(1, 99)
    return s


def lotto_gen():
    temp = []
    count2 = 6
    while count2 > 0:
        temp.append(num_gen())
        count2 -= 1
    return temp


def list_gen():
    temp_list = []
    i = 2
    while i > 0:
        temp_list.append(lotto_gen())
        i -= 1

   # print(f'{temp_list} ')
   # print(len(temp_list))
    # print(temp_list)
    return temp_list

# everything above generates list of n lotto numbers and also the pick six numbers


def win_checker(ticket_list, win):
    my_tickets = ticket_list
    winning_number = win
    match_count = 0
    money_spent = 0
    num = 0
    length = len(my_tickets)
    print(length)
    while length >= 0:
        while num < 6:
            if my_tickets[length-1][num] == winning_number[num]:
                match_count += 1
            else:
                pass
        num += 1
        money_spent += 2
        length -= 1

        print(match_count)
        print(winning_number)
        print(my_tickets)
        print(length)
        print(money_spent)


x = list_gen()
y = pick_six()


win_checker(x, y)
