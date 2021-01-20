

print('Practice 1: Fundamentals')

def is_even(a):
    # if a == 0:
    #     return False
    # elif a%2 == 0 :
    #     return True
    # else:
    #     return False
    return bool (a%2 == 0)

print('Problem 1')
print(is_even(5)) # False
print(is_even(6)) # True

def opposite(a, b):
    if a > 0:
        acheck = True
    else:
        acheck = False
    if b > 0:
        bcheck = True
    else:
        bcheck = False
    return acheck^bcheck # XOR

print('Problem 2')
print(opposite(10, -1)) # True
print(opposite(2, 3)) # False
print(opposite(-1, -1)) # False

def near_100(num):
    return bool((num >= -10 and num <=10)or(num >= 90-10 and num <=110)) # Ranges close to 10
 
print('Problem 3')
print(near_100(50)) # False
print(near_100(99)) # True
print(near_100(105)) # True

def maximum_of_three(a, b, c):
    return max(a,b,c) #max() Function Returns the largest

print('Problem 4')
print(maximum_of_three(5,6,2)) # 6
print(maximum_of_three(-4,3,10)) # 10

def print_powers_2():
    for x in range (0, 21): # Looping 20 times power of 2 (0 - 20)
        print(2**x,end=", ")

print('Problem 5')
print_powers_2() # 1, 2, 4, 8, 16, 32, ...
