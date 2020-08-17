# 071 
# Create a list of two sports. Ask the user what their favourite 
# sport is and add this to the end of the list. Sort the list 
# and display it. 
from typing import List


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

    sports_list = ['Badminton', 'Football']
    print(print_list(sports_list))

    user_sport = input('Enter your favourite sport: ')
    sports_list.append(user_sport)
    sports_list.sort()

    print(print_list(sports_list))

