# 090
# Ask the user to enter numbers. If they enter a number between 10
# and 20, save it in the array, otherwise display the message
# “Outside the range”. Once five numbers have been successfully
# added, display the message “Thank you” and display the array
# with each item shown on a separate line.

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

    numar = ar.array('i')

    for i in range(5):
        while True:
            user_input = get_num_int(f'Enter number {i+1}: ')
            if 10 > user_input or 20 < user_input:
                print('Please enter a number between 10 and 20')
            else:
                numar.append(user_input)
                break

    print('Thank you.')
    print(numar)

    # Using numpy module

    numnp = np.array([], dtype=np.int32)

    for i in range(5):
        while True:
            user_input = get_num_int(f'Enter number {i+1}: ')
            if 10 > user_input or 20 < user_input:
                print('Please enter a number between 10 and 20')
            else:
                numnp = np.append(numnp, user_input)
                break

    print('Thank you.')
    print(numnp)



