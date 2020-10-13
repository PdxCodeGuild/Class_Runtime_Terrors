



import random

# Problem 1 ====================================================

# Write a function using random.randint to generate an index, 
# use that index to pick a random element of a list and return it.

def random_element(a):
    i = random.randint(0, len(a)-1)
    return a[i]
# print(random_element(['apples', 'bananas', 'pears'])) # 'apples', 'bananas' or 'pears'


# Problem 2 ====================================================

# Write a function that takes a list of numbers, 
# and returns True if there is an even number of even numbers.
def eveneven(a):
    evencount = 0
    for even in a:
        if even % 2 == 0:
            evencount += 1
    if evencount != 0:
        if evencount %2 == 0:
            return True
        else: 
            return False
    else:
        return False
        

# print(eveneven([5, 6, 2])) # True
# print(eveneven([5, 5, 3])) # False

# Problem 3 ====================================================

# Write a function that returns the reverse of a list.

def reverse(nums):
    # newlist = list(reversed(nums))
    
    return nums [::-1]
    
    # newlist = nums.copy()
    # newlist.reverse()
    #return newlist

# print(reverse([1, 2, 3])) # 3, 2, 1



# Problem 4 ====================================================

# Write a function to move all the elements of a list with value less than 10 to a 
# new list and return it.

# list.append()

def extract_less_than_ten(nums):
    newlist = []      #Iterate over elements
    for num in nums:
        if num < 10:
            newlist.append(num)
    return newlist

    # newlist = []    #Iterate over indices
    # for i in range(len(nums)):
    #     if nums[i] < 10:
    #         newlist.append(nums[i])
    # return newlist

    # return [num for num in nums if num < 10]
    
# print(extract_less_than_ten([2, 8, 12, 18])) # [2, 8]





# Problem 5 ====================================================

# Write a function to find all common elements between two lists.

# number of iterations would be len(nums1)*len(nums2)
#   0  1  2
# 0 00 01 02
# 1 10 11 12
# 2 20 21 22

def common_elements(nums1, nums2):
    # newlist = []
    # for i in range(len(nums1)):
    #     for j in range(len(nums2)):
    #         print(i, j)
    #         if nums1[i] == nums2[j]:
    #             newlist.append(nums1[i])
    # return newlist

    newlist = []
    for num1 in nums1:
        if num1 in nums2:
            newlist.append(num1)
    return newlist

    # return [nums1[i] for i in range(len(nums1)) if nums1[i] == nums2[i]]
    # return [[1 if i == j else 0 for i in range(3)] for j in range(3)]
    return [num1 for num1 in nums1 if num1 in nums2]

print(common_elements([1, 2, 3], [2, 3, 4])) # [2, 3]

