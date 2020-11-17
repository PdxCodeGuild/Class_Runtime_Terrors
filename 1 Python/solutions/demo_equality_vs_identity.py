


# 'is' tests for identity
# '==' tests for equality

# x = 'hello!'
# y = 'hello'
# y += '!'
# x = 5
# y = 4
# y += 1
# print(x)
# print(id(x))
# print(y)
# print(id(y))

# if x == y: # equality
#     print('x == y')
# else:
#     print('x != y')

# if x is y: # identity
#     print('x is y')
# else:
#     print('x is not y')



# x = None
# y = None
# z = None
# print(id(x))
# print(id(y))
# print(id(z))

# x = None
# print(type(x))
# if x is None: # proper way
# if x == None: # improper way


# d1 = {'apples': 1}
# d2 = {'apples': 1}
# print(id(d1))
# print(id(d2))
# print(d1 == d2)





# immutable types
# None, boolean, int, float, string, tuple

# mutable types
# list, dictionary





# x = 'hello'
# x = x.upper()
# print(x)

# x = []
# x = x.append('a')
# print(x)



# x = 5
# y = x
# print(id(x))
# print(id(y))
# y += 1
# print(id(x))
# print(id(y))
# print(x)

x = ['a', 'b']
y = x # x.copy()
print(id(x))
print(id(y))
y.append('c')
print(id(x))
print(id(y))
print(x)








