# PDX Fullstack Practice: Three Lists
# Problem 1: pick a random element from a list
import random
def random_element(text):
    y = len(text) - 1
    x = random.randint(0, y)
    return(text[x])

#print(random_element(['apples', 'bananas', 'pears'])) 

# Problem 2: true IF there is an even number of even numbers
def eveneven(text):
    x = 0
    for i in range(len(text)):
        if (text[i] % 2):
            x += 1
    if x % 2:
        return True
    else: 
        return False


#print(eveneven([5, 6, 2])) # T
#print(eveneven([5, 5, 2])) # F

# Problem 3: reverse a given list
def reverse(text):
    text.reverse()
    return(text)

#print(reverse([1, 2, 3,]))

# Problem 4: return new list of items less than 10 from old list
def extract_less_than_ten(text):
    num = []
    for i in range(len(text)):
        if (text[i] < 10):
            num.append(text[i])
    return(num)

#print(extract_less_than_ten([2, 8, 12, 18]))

# Problem 5: return all common elements shared in two lists
def common_elements(num1, num2):
    num = []
    if num1 > num2:
        num3 = num1
    else:
        num3 = num2
    for i in range(len(num3)):
        if (num2[i] in num1):
            num.append(num2[i])
    return(num)


#print(common_elements([1,2,3], [2,3,4]))

# Problem 6: new list alternate elements of two lists
def combine(num1, num2):
    num = []
    for i in range(len(num1)):
        num.append(num1[i])
        num.append(num2[i])
    return(num)


#print(combine(['a', 'b', 'c'], [1,2,3]))

# Problem 7: return any two elements of a list whose sum is a given target
def find_pair(nums, tgt):
    n = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if ((nums[i] + nums[j]) == tgt):
                if (nums[i] not in n):
                    n.append(nums[i])
                if (nums[j] not in n):
                    n.append(nums[j])
        
                
    return(n)


#print(find_pair([5,6,2,3], 7))

# Problem 8: return AVG of a list of nums
def average(nums):
    l = len(nums)
    x = 0
    for i in range(l):
        x = x + nums[i]

    return(int(x / l))


#print(average([1,2,3,4,5]))

# Problem 9: rmv all empty strings from a list
def remove_empty(text):
    for i in range(len(text)):
        try:
            text.remove('')
        except ValueError:
            break
    return(text)

#print(remove_empty(['a', 'b', '', 'c', '', 'd']))

# Problem 10: create a new list of lists where each element in a two \
# + element pair is 1 element from each of the original two lists
def merge(nums1, nums2):
    n = [] # new list of lists
    m = [] # stores value pairs
    for i in range(len(nums1)):
        m.append(nums1[i])
        m.append(nums2[i])
        n.append(m)
        m = []
    return(n)



#print(merge([5,2,1], [6,8,2]))

# Problem 11: combine all elements of 3 lists into new list
def combine_all(nums1, nums2, nums3):
    n = []
    for i in range(len(nums1)):
        n.append(nums1[i])
    for i in range(len(nums2)):
        n.append(nums2[i])
    for i in range(len(nums3)):
        n.append(nums3[i])
    return(n)


#print(combine_all([5,2,3], [4,5,1], [7,6,3]))

# Problem 12: generate a list of Fibonacci numbers from given number \
# + of length equal to the given number
def fibonacci(num):
    n = [] 
    i = 0   # counter
    f1 = 0  # fibonnaci f1
    f2 = 1  # fibonacci f2
    while i < num: 
        x = f1 + f2    # f3 = f1 + f2
        n.append(x)     # capture result
        i += 1          # count up
        f1 = f2        # set f1 to f2
        f2 = x          # set f2 to f3
        
    return(n)

#print(fibonacci(8))

# Problem 13: reutrn factorial of a given number
def factorial(n):
    f = 1
    i = 1
    while i < (n+1):
        f = f * i
        i += 1
    return(f)


#print(factorial(5))

# Problem 14: remove duplicates from given list
def find_unique(nums):
    n = []
    for i in range(len(nums)):
        if nums[i] not in n:
            n.append(nums[i])

    return(n)


print(find_unique([12, 24, 35, 24,88, 120, 155, 120, 155]))