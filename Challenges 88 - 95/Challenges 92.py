# 092
# Create two arrays (one containing three numbers that the user
# enters and one containing a set of five random numbers). Join
# these two arrays together into one large array. Sort this large
# array and display it so that each number appears on a separate line

import array as ar
import random
import numpy as np
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


if __name__ == '__main__':

    # Using built in array module

    numar = ar.array('i', create_random_list(length=5))

    print(numar)

    user_input = ar.array('i')
    for i in range(3):
        user_input.append(get_num_int(f'Enter number {i+1}: '))

    numar.extend(user_input)
    numar = sorted(numar)

    for i in range(len(numar)):
        print(numar[i])

    # Using numpy module

    numnp = np.array(create_random_list(length=5), dtype=np.int8)

    print(numnp)

    user_input = np.array([], dtype=np.int8)
    for i in range(3):
        user_input = np.append(user_input,
                               get_num_int(f'Enter number {i + 1}: '))

    numnp = np.append(numnp, user_input)
    numnp = np.sort(numnp)

    for i in range(len(numnp)):
        print(numnp[i])


