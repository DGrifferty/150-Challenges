# 048
# Ask for the name of somebody the user wants to invite to a party.
# After this, display the message “[name] has now been invited” and
# add 1 to the count. Then ask if they want to invite somebody else.
# Keep repeating this until they no longer want to invite anyone else
# to the party and then display how many people they have coming to
# the party.

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


def print_list(lst: List[float]):
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

    while True:

        name = input('Who would you like to invite to your party?: ')
        invite_list.append(name.title())
        print(f'{name.title()} has now been invited.')
        if not yes_no_checker('Would you like to invite '
                              'someone else?: '):
            break

    print(f'The following have been invited: {print_list(invite_list)}')

