





# big o is a description of the complexity of an algorithm
# time complex - relationship between the size of the input and the number of steps needed to solve the problem
# space complexity - relationship between the size of the input and the amount of memory required to solve the problem
# independent of any particular hardware configuration or programming language


# total cost = 2*allocation + n*(comparison + list_access + 2*sum) + return

import time
import random
import matplotlib.pyplot as plt





# O(1)
def random_element(numbers):
    return numbers[random.randint(0, len(numbers)-1)]




# O(n)
def calculate_total(numbers):
    total = 0 # allocate an int
    i = 0 # allocate an int
    while i < len(numbers): # comparison
        total += numbers[i] # list access and sum
        i += 1 # sum
        global counter
        counter += 1
    return total # return


# for list_size in range(1000, 2000):
#     trial_sum = 0
#     for i in range(20):
#         start_time = time.time()
#         numbers = [random.randint(1, 99) for j in range(list_size)]
#         calculate_total(numbers)
#         end_time = time.time()
#         trial_time = end_time - start_time
#         trial_sum += trial_time
#     trial_average = trial_sum / 10
#     print(list_size, trial_average)


# O(n^2)
def common_elements(nums1, nums2):
    output = []
    for num1 in nums1:
        for num2 in nums2:
            if num1 == num2:
                output.append(num1)
            global counter
            counter += 1
    return output

# number_of_trials = 20
# for list_size in range(2, 400):
#     trial_sum = 0
#     for i in range(number_of_trials):
#         global counter
#         counter = 0
#         numbers = [random.randint(1, 99) for j in range(list_size)]
#         common_elements(numbers[:len(numbers)//2], numbers[len(numbers)//2:])
#         trial_sum += counter
#     trial_average = trial_sum / number_of_trials
#     print(list_size, trial_average)

# O(n!)
def bogosort(nums):
    while True:
        random.shuffle(nums)
        is_sorted = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                is_sorted = False
                break
            global counter
            counter += 1
        if is_sorted:
            break
        





# number_of_trials = 20
# for list_size in range(2, 10):
#     trial_sum = 0
#     for i in range(number_of_trials):
#         global counter
#         counter = 0
#         numbers = [random.randint(1, 99) for j in range(list_size)]
#         bogosort(numbers)
#         trial_sum += counter
#     trial_average = trial_sum / number_of_trials
#     print(list_size, trial_average)


# O(n)
def linear_search(nums, target):
    for i in range(len(nums)):
        global counter
        counter += 1
        if nums[i] == target:
            return i
    return None





# x_values = []
# y_values = []

# number_of_trials = 5000
# start_size = 500
# end_size = 1000
# step_size = 100

# number_of_trials = 1000
# start_size = 1
# end_size = 256
# step_size = 1

# for list_size in range(start_size, end_size, step_size):
#     trial_sum = 0
#     for i in range(number_of_trials):
#         global counter
#         counter = 0
#         numbers = [random.randint(1, 99) for j in range(list_size)]
#         numbers.sort()
#         linear_search(numbers, random.choice(numbers))
#         trial_sum += counter
#     trial_average = trial_sum / number_of_trials
#     x_values.append(list_size)
#     y_values.append(trial_average)
#     print(list_size, trial_average)

# plt.plot(x_values, y_values)
# plt.show()



# O(log(n))
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        global counter
        counter += 1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1 # look in the upper half
        elif nums[mid] > target:
            high = mid - 1 # look in the lower half
    return None
        


# x_values = []
# y_values = []

# number_of_trials = 1000
# for list_size in range(1, 2**8, 1):
#     trial_sum = 0
#     for i in range(number_of_trials):
#         global counter
#         counter = 0
#         numbers = [random.randint(1, 99) for j in range(list_size)]
#         numbers = list(set(numbers))
#         numbers.sort()
#         target_index = random.randint(0, len(numbers)-1)
#         binary_search(numbers, numbers[target_index])
#         trial_sum += counter
#     trial_average = trial_sum / number_of_trials
#     x_values.append(list_size)
#     y_values.append(trial_average)
#     print(list_size, trial_average)

# plt.plot(x_values, y_values)
# plt.show()




