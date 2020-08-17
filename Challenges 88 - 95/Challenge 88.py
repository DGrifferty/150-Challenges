# Challenges 88 - 95 will be done in both the array and numpy modules

# 088
# Ask the user for a list of five integers. Store them in an array.
# Sort the list and display it in reverse order.

import array as ar
import numpy as np


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))
            return number

        except Exception as e:
            print(e)


if __name__ == '__main__':

    # # Using built in array module
    # nums = ar.array('i')
    # for i in range(5):
    #     nums.append(get_num_int(f'Enter number {i + 1}: '))
    # print(sorted(nums, reverse=True))

    # Using numpy

    nums = np.array([], dtype=np.int32)
    for i in range(5):
        nums = np.append(nums, get_num_int(f'Enter number {i + 1}: '))

    print(np.flipud(np.sort(nums)))



