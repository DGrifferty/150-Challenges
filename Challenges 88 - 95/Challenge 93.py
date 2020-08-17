# 093
# Ask the user to enter five numbers. Sort them into order and
# present them to the user. Ask them to select one of the numbers.
# Remove it from the original array and save it in a new array.

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

    # Using built in array module

    user_ar = ar.array('i')

    for i in range(5):
        user_ar.append(get_num_int(f'Enter number {i + 1}: '))

    user_ar = sorted(user_ar)
    print(user_ar)

    while True:

        num = get_num_int('Please select a number to remove - ')

        if num in user_ar:
            user_removed = ar.array('i', [num])
            user_ar.remove(num)
            break

    print(user_ar)
    print(user_removed)

    # Using numpy module

    user_np = np.array([], dtype=np.int32)

    for i in range(5):
        user_np = np.append(user_np,
                            get_num_int(f'Enter number {i + 1}: '))

    user_np = np.sort(user_np)
    print(user_np)

    while True:

        num = get_num_int('Please select a number to remove - ')

        if num in user_np:
            user_removed_np = np.array(num, dtype=np.int32)
            user_np = np.delete(user_np, np.argwhere(user_np == num))
            break

    print(user_np)
    print(user_removed_np)
