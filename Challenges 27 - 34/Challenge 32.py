# 032
# Ask for the radius and the depth of a cylinder and work out the total
# volume (circle area*depth) rounded to three decimal places.

from math import pi
from typing import List


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
                assert len(num) >= min_length, f'Please enter at least'\
                                              f' {min_length} numbers'
            if max_length:
                assert len(num) <= max_length, f'Please enter no more '\
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


if __name__ == '__main__':
    request = 'Please enter the radius and the height of the you would ' \
              'like to calculate the volume for: '

    volume = cylinder_volume(check_num_list(request, 2, 2))

    print(f'Volume of cylinder - {round(volume, 3)}')
