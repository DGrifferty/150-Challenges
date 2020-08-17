# 089
# Create an array which will store a list of integers.
# Generate five random numbers and store them in the array.
# Display the array (showing each item on a separate line).

import random
import array as ar
import numpy as np
from typing import List


def create_random_list(length: int = 50, lowest_num: int = 0,
                       highest_num: int = 90) -> List[int]:
    """Returns a random list at a user set len, and lower and upper
    bounds"""

    # used to test return_index function

    random_list = list()

    for i in range(length):
        random_list.append(random.randint(lowest_num, highest_num))

    return random_list


if __name__ == '__main__':

    # Using built in array module

    nums = ar.array('i', create_random_list(length=5))

    for index, value in enumerate(nums):
        print(value)


    npnums = np.array(create_random_list(length=5), dtype = np.int32)

    for index, value in enumerate(npnums):
        print(value)






