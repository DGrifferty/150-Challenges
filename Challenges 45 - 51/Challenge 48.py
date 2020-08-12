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


if __name__ == '__main__':


    while True:
        



    print(f'After adding the following:\n{print_list(summed)}')
    print(f'The final total is: {sum(summed)}')