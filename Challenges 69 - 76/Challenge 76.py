# 076
# Ask the user to enter the names of three people they want to invite
# to a party and store them in a list. After they have entered all
# three names, ask them if they want to add another. If they do,
# allow them to add more names until they answer “no”. When they
# answer “no”, display how many people they have invited to the party

# Similar to challenge 48

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


