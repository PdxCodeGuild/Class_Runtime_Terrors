

# import random



# # automatic tuple packing
# t = 5, 6
# print(t)

# # automatic tuple unpacking
# t = (5, 6)
# a, b = t
# print(a)
# print(b)


# def get_dimensions():
#     return 5, 6
# t = get_dimensions()
# print(t)
# width, height = get_dimensions()
# print(width)
# print(height)


# fruits = ['apples', 'bananas', 'pears']
# t = fruits[0]
# fruits[0] = fruits[1]
# fruits[1] = t

# print(fruits)
# fruits[0], fruits[1] = fruits[1], fruits[0]

# print(fruits)





def get_value(value):
    if value == 'A':
        return 1
    elif value in ['J', 'Q', 'K']:
        return 10
    else:
        return int(value)



# suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
# values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# # print(len(suites)*len(values))

# deck = []
# for suit in suits:
#     for value in values:
#         # deck.append((value, suit)) # append a tuple to the list
#         deck.append({
#             'suit': suit,
#             'value': value,
#             'letter_value': value[0],
#             'numerical_value': get_value(value[0])
#         })

# random.shuffle(deck)

# card = deck.pop(random.randint(0, len(deck)-1))
# print('You got ' + card['value'] + ' of ' + card['suit'])




card_values = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

card1 = input('what is your first card? ')
card2 = input('what is your second card? ')
card3 = input('what is your third card? ')

cards = [card1, card2, card3]
totals = [0]
for card in cards:
    if card == 'A':
        totals_1 = totals
        totals_11 = totals.copy()
        for i in range(len(totals_1)):
            totals_1[i] += 1
        for i in range(len(totals_11)):
            totals_11[i] += 11
        totals = totals_1 + totals_11
    else:
        for i in range(len(totals)):
            totals[i] += card_values[card]
totals = list(set(totals))
totals.sort()

for total in totals:
    if total < 17:
        print(total, 'hit')
    elif total < 21:
        print(total, 'stay')
    elif total == 21:
        print(total, 'blackjack')
    else:
        print(total, 'bust')

# total = card_values[card1] + card_values[card2] + card_values[card3]
# if total < 17:
#     print(total, 'hit')
# elif total < 21:
#     print(total, 'stay')
# elif total == 21:
#     print(total, 'blackjack')
# else:
#     print(total, 'bust')






