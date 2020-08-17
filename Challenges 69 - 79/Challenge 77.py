# 077
# Change program 076 so that once the user has completed their
# list of names, display the full list and ask them to type in
# one of the names on the list. Display the position of that name
# in the list. Ask the user if they still want that person to come
# to the party. If they answer “no”, delete that entry from the list
# and display the list again.
from typing import List


def yes_no_checker(string):
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


def print_list(lst: List):
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

    invite_list = list()

    for i in range(3):
        name = input('Who would you like to invite to your party?: ')
        invite_list.append(name.title())
        print(f'{name.title()} has now been invited.')

    while True:

        if not yes_no_checker('Would you like to invite '
                              'someone else?: '):
            break

        name = input('Who would you like to invite to your party?: ')
        invite_list.append(name.title())
        print(f'{name.title()} has now been invited.')

    print(f'The following have been invited: {print_list(invite_list)}')

    while True:

        name = input('Enter name of someone on the list: ')
        name = name.title()

        if name.title() in invite_list:
            print(f'{name} is at position'
                  f' {invite_list.index(name)}')
            break

    if not yes_no_checker('Would you still like them '
                          'to come to the party?'):
        invite_list.remove(name)
        print(f'The following have been invited: '
              f'{print_list(invite_list)}')




