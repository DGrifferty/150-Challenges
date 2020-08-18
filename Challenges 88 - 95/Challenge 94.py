# 094
# Display an array of five numbers. Ask the user to select one
# of the numbers. Once they have selected a number, display the
# position of that item in the array. If they enter something that
# is not in the array, ask them to try again until they select
# a relevant item.

import array as ar
import numpy as np
import random
from typing import List


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))
            return number

        except Exception as e:
            print(e)


def create_random_list(length: int = 50, lowest_num: int = 0,
                       highest_num: int = 90) -> List[int]:
    """Returns a random list at a user set len, and lower and upper
    bounds"""

    # used to test return_index function

    random_list = list()

    for i in range(length):
        random_list.append(random.randint(lowest_num, highest_num))

    return random_list


def return_index(tp, element) -> List[int]:
    """Returns all the indexes of an element"""

    indexes = []
    [indexes.append(index) for index, value in enumerate(tp)
     if value == element]

    return indexes


if __name__ == '__main__':

    # Using built in array module

    nums_ar = ar.array('i', create_random_list(5))

    print(nums_ar)

    while True:

        num = get_num_int('Please select a number to get the index of'
                          '- ')

        if num in nums_ar:
            print(f'Index(s) of {num} are at '
                  f'{return_index(nums_ar, num)}')
            break

    # Using numpy module

    nums_np = np.array(create_random_list(5), dtype=np.int32)

    print(nums_np)


    while True:

        num = get_num_int('Please select a number to get the index of'
                          '- ')

        if num in nums_np:
            print(f'Index(s) of {num} are at '
                  f'{return_index(nums_np, num)}')
            break

