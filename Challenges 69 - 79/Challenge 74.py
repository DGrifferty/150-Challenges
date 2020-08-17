# 074
# Enter a list of ten colours. Ask the user for a starting number
# between 0 and 4 and an end number between 5 and 9. Display the
# list for those colours between the start and end numbers the user
# input.
from typing import List


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


def print_list(lst: List[float]):
    """returns a string allowing you to print a list in a cleaner way"""

    string = ''

    for i in range(len(lst)):

        if i == len(lst) - 1:
            string += f'{lst[i]}.'
        else:
            string += f'{lst[i]}, '

        if i > 0:
            if i % 10 == 0:
                string += '\n'

    return string


if __name__ == '__main__':

    colour_list = ['Red', 'Blue', 'Violet', 'Orange', 'Purple', 'white',
                   'Pink', 'Grey', 'Yellow', 'Green']

    while True:
        start = get_num_int('Enter starting number: ')

        if 0 <= start <= 4:
            break
        else:
            print('Please enter a number between 0 and 4')

    while True:
        end = get_num_int('Enter an end number: ')

        if 5 <= end <= 9:
            break
        else:
            print('Please enter a number between 5 and 9')

    print(print_list(colour_list[start:end]))
