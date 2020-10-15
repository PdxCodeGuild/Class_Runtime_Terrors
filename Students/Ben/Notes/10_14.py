# temperature = 70

# # if temperature < 90:
# #   if 60 < temperature < 68:
# #     print('Hot')
# #   elif 69 < temperature <80:
# #     print("Really Hot")
# # elif temperature < 60:
# #   print("Cold")

# # def truthy_falsey(a):
# #   return 'Truthy'if a else 'falsey'

# # print(truthy_falsey(0))

# def true_or_false(a):
#   return "true" if a >10 else 'fasle'

# print(true_or_false(12)) 

# sentence = "Hello World"
# print(sentence[5:8])

# sentence = "Hello World"
# print(sentence[5:])

# sentence = "Hello World"
# print(sentence[::3])

# sentence = "Hello World" 
# print(sentence[::-1]) # reverse 

# sentence = ['bread', 'potatoes', 'coffee', 'pasta', 'rice', 'sugar', 'shoes','socks']
# print(sentence[0:7:2]) # will display 'bread', 'coffee', "rice", 'shoes' #


# x = 5
# print(id(x)) # unique location of this object  '1361639408'#
# y = x
# print (id(y)) # 1361639408 for both x and y #

# print(id(x) == id(y))  #"Ture"
# print(id(x) is id(y))  #"False"

# x = 5
# print(id(x)) #1361639408
# x = 6
# print(id(x)) #1361639424

shopping_list = ['a','b','c','d']
print(id(shopping_list)) #51834408
shopping_list[0] = '-a'
print(id(shopping_list)) #51834408
print(shopping_list) # ['-a', 'b', 'c', 'd']
