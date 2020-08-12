# 034
# Display the following message:
# If the user enters 1, then it should ask them
# for the length of one of its sides and display the area.If they select
# 2, it should ask for the base and height of the triangle and display
# the area.If they type in anything else, it should give them a
# suitable error message.

from typing import List


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


def square_area(side_length: float) -> float:
    return side_length * side_length


def triangle_area(base_height: List[float]) -> float:
    return 0.5 * base_height[0] * base_height[1]


if __name__ == '__main__':

    if square_or_triangle():
        request = 'Enter length of the squares sides: '
        print(f'The square has an area of: '
              f'{square_area(float(check_num_list(request, 1, 1)[0]))}')
    else:
        request = 'Enter the base and the height of the triangle: '
        print(f'The triangle has an area of: '
              f'{triangle_area(check_num_list(request, 2, 2))}')
