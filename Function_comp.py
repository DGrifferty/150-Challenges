from typing import List, Tuple
from math import pi
import math


def check_input_str_num(prompt: str) -> Tuple[str, int]:
    while True:
        try:
            user_input = input(prompt)

            user_input = user_input.split(', ')

            if len(user_input) != 2:
                raise Exception('Please enter your name and a number'
                                'separated by - \', \' (a comma and'
                                'space)')

            return user_input[0], int(user_input[1])

        except Exception as e:
            print(e)

def check_num(prompt: str) -> float:
    """Function to check if users input is a num"""

    while True:
        try:
            num = float(input(prompt))

            return num

        except Exception as e:
            print(e)


def input_checker(string):
    yes_list = ['yes', 'y', '1']
    no_list = ['no', 'n', '0']
    while True:
        try:

            answer = input(string)

            if answer.lower() not in yes_list and answer.lower() \
                    not in no_list:
                print('Please enter yes or no!')
                continue
            elif answer.lower() in yes_list:
                return True
            else:
                return False

        except Exception as e:
            print(e)


def length(s1: str, l: int = 5) -> bool:
    if len(s1) < l:
        return True
    return False


def convert_pig(words):
    for index, value in enumerate(words):

        if words[index][0].lower() in 'aeiou':
            words[index] = words[index] + 'way'
            continue

        first_consonant = words[index][0]

        words[index] = words[index][1:] + first_consonant + 'ay'

    return words


def check_num_list(prompt: str, max_length: int = 0,
                   min_length: int = 0) -> List[float]:
    """Function to check if users input is a number, splitting number
    by spaces and checking that the correct amount of numbers are
    entered, returning them in a list"""

    while True:
        try:
            num = input(prompt)
            num = num.split(' ')
            if min_length:
                assert len(num) >= min_length, f'Please enter at least' \
                                               f' {min_length} numbers'
            if max_length:
                assert len(num) <= max_length, f'Please enter no more ' \
                                               f'than {max_length} ' \
                                               f'numbers'
            for index, value in enumerate(num):
                num[index] = float(value)

            return num

        except Exception as e:
            print(e)


def circle_area(radius: float) -> float:
    """Calculates area of a circle from a given radius"""
    return pi * radius ** 2


def cylinder_volume(radius_height: List[float]) -> float:
    """Calculates the volume of a cylinder from a given radius and
    height, from  a list"""

    return circle_area(radius_height[0]) * radius_height[1]


def integer_devision_remainder(nums: List[float]) -> str:
    return f'{nums[0]} / {nums[1]} = {nums[0] // nums[1]} with' \
           f' a remainder of {nums[0] % nums[1]}'


def square_area(side_length: float) -> float:
    return side_length * side_length


def triangle_area(base_height: List[float]) -> float:
    return 0.5 * base_height[0] * base_height[1]


def square_or_triangle() -> bool:
    print('Would you like to calculate the area of a square or '
          'triangle?')
    while True:
        try:

            print('1) square\n2) triangle')
            choice = int(input('Choose an option: '))

            if choice != 1 and choice != 2:
                raise Exception('Please enter 1 or 2.')

            if choice == 1:
                return True
            else:
                return False

        except Exception as e:
            print(e)
