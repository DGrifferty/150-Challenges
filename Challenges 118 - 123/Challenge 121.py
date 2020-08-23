# 121
# Create a program that will allow the user to easily manage a
# list of names. You should display a menu that will allow them
# to add a name to the list, change a name in the list, delete a
# name from the list or view all the names in the list. There
# should also be a menu option to allow the user to end the program.
# If they select an option that is not relevant, then it should
# display a suitable message. After they have made a selection
# to either add a name, change a name, delete a name or view
# all the names, they should see the menu again without having
# to restart the program. The program should be made as easy
# to use as possible.
from typing import List


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))
            return number

        except Exception as e:
            print(e)


def get_index_in_list(lst: List) -> int:
    while True:
        index = get_num_int(f'Enter index between 0 and '
                            f'{len(lst) - 1}: ')
        if 0 <= index < len(lst):
            return index


def print_list_with_index(lst: List) -> None:
    string = ''
    for index, value in enumerate(lst):
        string += f'{index}: {value}, '
        if index > 0 and index % 10 == 0:
            string += '\n'
    print(string)
    return string


def change_element(lst: List, index) -> List:
    new_value = input('Enter new value: ')
    lst[index] = new_value
    return lst


def remove_element(lst: List, index) -> List:
    lst.pop(index)
    return lst


def get_menu_choice() -> int:
    menu = '''-------------
1) Print list
2) Change element in List
3) Remove element from list
4) Exit
Enter 1, 2 or 3: '''
    while True:
        choice = get_num_int(menu)
        if 1 <= choice <= 4:
            print('-------------')
            break
    return choice


if __name__ == '__main__':

    lst1 = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5']
    print_list_with_index(lst1)

    while True:
        choice = get_menu_choice()

        if choice == 1:
            print_list_with_index(lst1)
        elif choice == 2:
            print_list_with_index(lst1)
            change_element(lst1, get_index_in_list(lst1))
            print('-------------\nElement changed\n-------------')
            print_list_with_index(lst1)
        elif choice == 3:
            print_list_with_index(lst1)
            remove_element(lst1, get_index_in_list(lst1))
            print('-------------\nElement removed\n-------------')
            print_list_with_index(lst1)
        elif choice == 4:
            print('Thank you!')
            break
