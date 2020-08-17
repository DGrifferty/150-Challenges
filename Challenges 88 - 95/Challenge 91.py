# 091
# Create an array which contains five numbers (two of which
# should be repeated). Display the whole array to the user.
# Ask the user to enter one of the numbers from the array
# and then display a message saying how many times that
# number appears in the list.

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
            
    
def return_index(tp, element) -> List[int]:
    """Returns all the indexes of an element"""

    indexes = []
    [indexes.append(index) for index, value in enumerate(tp)
     if value == element]

    return indexes


if __name__ == '__main__':
    
    # Using built in array module
    
    numar = ar.array('i')
    for i in range(5):
        if i < 4:
            numar.append(random.randint(1, 100))
        elif i == 4:
            numar.append(numar[random.randint(0, 4)])

    print(numar)
    
    while True:
        
        user_input = get_num_int('Enter a number from the above array: ')
        
        if user_input in numar:

            print(f'Number at indexes - '
                  f'{return_index(numar, user_input)}')
            break


    # Using numpy modules

    numnp = np.array([], dtype=np.int32)

    for i in range(5):
        if i < 4:
            numnp = np.append(numnp, random.randint(1, 100))
        elif i == 4:
            numnp = np.append(numnp, numnp[random.randint(0, 4)])

    print(numnp)

    while True:

        user_input = get_num_int(
            'Enter a number from the above array: ')

        if user_input in numnp:
            print(f'Number at indexes - '
                  f'{return_index(numnp, user_input)}')
            break

    

    
    
    
