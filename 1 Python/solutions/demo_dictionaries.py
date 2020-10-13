
# fruits = [
#     'apples',
#     'bananas',
#     'pears'
# ]
product_to_price = {
    'apples': 1.0,
    'bananas': 0.5,
    'kumquats': 2.0,
    'dragonfruit': 4.0
}

# print(product_to_price['blueberries'])
print(product_to_price.get('blueberries', 1))


print(product_to_price)
print(product_to_price['apples']) # 1.0
product_to_price['apples'] += 0.5
print(product_to_price)
product_to_price['blueberries'] = 1.2
print(product_to_price)

for product in product_to_price:
    print(product, product_to_price[product])

for product in product_to_price.keys():
    print(product, product_to_price[product])
for value in product_to_price.values():
    print(value)


# iterables - types you can use with a for-loop
# strings - iterate over the characters
# lists - iterate over the elements/items
# tuples - iterate over the elements/items
# dictionaries - iterate over the keys
# range - iterate over a range of numbers
# <list_reverseiterator object at 0x0341E700> - iterate over a reversed list/string
# dict_keys, dict_values, dict_items
print(list(product_to_price.keys()))
print(list(product_to_price.values()))
print(list(product_to_price.items()))
print(list(range(5)))
print(list(reversed([1, 2, 3])))
# for num in reversed([1, 2, 3]):
#     print(num)


# keys can be any immutible type - None, boolean, int, float, string, tuple
# values can be any type
# fruits = {
#     0: 'apples',
#     1: 'bananas',
#     2: 'pears'
# }
# print(fruits[0])


total = 0
counter = 0
for product in product_to_price:
    total += product_to_price[product]
    counter += 1
print('average is', total/counter)
print('average is', total/len(product_to_price))




alphabet = 'abcdefghijklmnopqrstuvwxyz'
rotated_alphabet = alphabet[13:] + alphabet[:13]
cipher = {}
for i in range(len(alphabet)):
    cipher[alphabet[i]] = rotated_alphabet[i]
print(cipher)
word = 'hello'
output = ''
for char in word:
    output += cipher[char]
print(output)






