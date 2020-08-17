# 078
# Create a list containing the titles of four TV programmes
# and display them on separate lines. Ask the user to enter
# another show and a position they want it inserted into the
# list. Display the list again, showing all five TV
# programmes in their new positions.
from typing import List


def print_list(lst: List):
    """prints a list in a cleaner way"""

    string = ''

    for i in range(len(lst)):

        if i == len(lst) - 1:
            string += f'{lst[i]}.'
        else:
            string += f'{lst[i]}, '

        if i > 0:
            if i % 10 == 0:
                string += '\n'

    print(string)


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


if __name__ == '__main__':

    shows = ['Show1', 'Show2', 'Show3', 'Show4']

    print_list(shows)

    new_show = input('Enter the show you would like to add to the '
                     'list: ')

    while True:


        position = get_num_int('Enter the position you would like to '
                    'put this show: ')
        
        if 0 <= position <= len(shows) + 1:
            break
        else:
            print(f'Please enter a number between 0 and '
                  f'{len(shows) +1 }')
            
    shows.insert(position, new_show)
    
    print_list(shows)
    
    

        







