# 052
# Display a random integer between 1 and 100 inclusive
import random

print(random.randint(1, 100))


# # A way to check it is inclusive without checking documentation
#
# nums = list()
#
# for i in range(2000):
#
#     nums.append(random.randint(1, 100))
#     print(nums[i])
#
# nums = set(nums)
#
# print(f'max: {max(nums)}')
# print(f'min: {min(nums)}')
