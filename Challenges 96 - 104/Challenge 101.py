# 101
# Using program 100, ask the user for a name and a region.
# Display the relevant data. Ask the user for the name
# and region of data they want to change and allow
# them to make the alteration to the sales figure.
# Display the sales for all regions for the name they choose

from typing import Dict

def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


def sort_dict(dic: Dict[int, str]) -> Dict[int, str]:
    """Sorts the keys into ascending order, filling in any gaps"""
    values = list(dic.values())
    print(values)
    dic.clear()

    for i in range(len(values)):
        print(i)
        print(values[i])
        dic[i + 1] = values[i]

    return dic


def print_dic(dic: Dict) -> str:
    """Allows you to print a dictionary in a cleaner way"""

    values = list(dic.values())
    keys = list(dic.keys())

    string = ''

    for i in range(len(keys)):

        if i == len(keys) - 1:
            string += f'{keys[i]} : {values[i]}.'
        else:
            string += f'{keys[i]} : {values[i]}, '

        if i > 0:
            if i % 10 == 0:
                string += '\n'

    return string


if __name__ == '__main__':

    sales = {
        'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
        'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
        'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
        'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
    }