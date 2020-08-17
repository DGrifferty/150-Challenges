# 093
# Ask the user to enter five numbers. Sort them into order and
# present them to the user. Ask them to select one of the numbers.
# Remove it from the original array and save it in a new array.

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

if __name__ == '__main__':

    
