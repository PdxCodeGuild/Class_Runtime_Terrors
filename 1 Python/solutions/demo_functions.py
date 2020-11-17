







# n! = n*(n-1)*(n-2)*...
# 5! = 5*4*3*2*1
# 10! = 10*9*8...
# def factorial(n):
#     output = 1
#     while n > 0:
#         output *= n
#         n -= 1
#     return output


# def factorial(n, depth):
#     print('\t'*depth, 'factorial(',n,')')
#     if n == 1:
#         print('\t'*depth, 'returning 1')
#         return 1
#     result = n*factorial(n-1, depth+1)
#     print('\t'*depth, 'returning', result)
#     return result

# print(factorial(5, 1))

# def say_hello():
#     print('hello')
#     main()

# def main():
#     x = 5
#     say_hello()

# main()




# def c():
#     message = 'c'
#     print(message)
#     print('returning from c')

# def b():
#     message = 'b'
#     print(message)
#     c()
#     print('returning from b')

# def a():
#     message = 'a'
#     print(message)
#     b()
#     print('returning from a')

# a()
# print('done')



# def peaks(llama):
#     data = 'hello'
#     print(data)

# data = [1, 2, 3]
# print(data)
# peaks(data)



def get_dimensions():
    return 5, 8

# d = get_dimensions()
# print(d)
# width = d[0]
# height = d[1]

width, height = get_dimensions()
print(width)
print(height)


fruits = ['apples', 'bananas', 'pears']
# swap the elements at index 0 and 1
temp = fruits[0]
fruits[0] = fruits[1]
fruits[1] = temp


fruits[0], fruits[1] = fruits[1], fruits[0]

print(fruits)







