# 095
# Create an array of five numbers between 10 and 100 which each
# have two decimal places. Ask the user to enter a whole number
# between 2 and 5. If they enter something outside of that range,
# display a suitable error message and ask them to try again until
# they enter a valid amount. Divide each of the numbers in the array
# by the number the user entered and display the answers shown to
# two decimal places.

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


def create_random_list_float(length: int = 5, low: int = 10, 
                             high: int = 90, dp: int = 2):
    return list(round(random.uniform(low, high), dp) for _ in range(length))


if __name__ == '__main__':

    # Using built in array

    rand_ar = ar.array('f', create_random_list_float())

    for i in range(len(rand_ar)):
        print(round(rand_ar[i], 2), end=',')

    print('')

    while True:
        try:
            num_ar = get_num_int('Enter a number to divide them by: ')

            if not 2 <= num_ar <= 5:
                raise Exception('The number must be between 2 and 5.')
            else:
                break
        except Exception as e:
            print(e)

    for i in range(len(rand_ar)):
        rand_ar[i] = rand_ar[i] / num_ar

    for i in range(len(rand_ar)):
        print(round(rand_ar[i], 2), end=',')

    # Using numpy module

    rand_np = np.array(create_random_list_float())

    print(rand_np)

    while True:
        try:
            num_np = get_num_int('Enter a number to divide them by: ')

            if not 2 <= num_np <= 5:
                raise Exception('The number must be between 2 and 5.')
            else:
                break
        except Exception as e:
            print(e)

    print(np.round(rand_np/num_np, 2))
