# 054
# Randomly choose either heads or tails (“h” or “t”).
# Ask the user to make their choice. If their choice is
# the same as the randomly selected value, display the message
# “You win”, otherwise display “Bad luck”. At the end,
# tell the user if the computer selected heads or tails.

import random

dev = False

def heads_tails_checker(string:str) -> bool:
    """Function to check user enters an accepted input, then returns
    input as boolean"""
    heads_list = ['heads', 'head', 'h', '1']
    tails_list = ['tails', 'tail', 't', '0']
    while True:
        try:
            answer = input(string)
            if answer.lower() not in heads_list and answer.lower() \
                    not in tails_list:
                print('Please enter heads or tails!')
                continue
            elif answer.lower() in heads_list:
                return True
            else:
                return False

        except Exception as e:
            print(e)


def yes_no_checker(string):
    """Function to check user enters yes or no, then returns
    input as boolean"""

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

    htlst = ['heads', 'tails']
    correct_count, guess_count = 0, 0

    while True:

        comp_choice = random.choice(htlst)

        if dev:
            print(comp_choice)

        users_choice = heads_tails_checker('Heads or tails?: ')
        guess_count += 1

        if users_choice and comp_choice == htlst[0] or not users_choice\
            and comp_choice == htlst[1]:
            print('Correct!')
            correct_count += 1
        else:
            print('Incorrect')

        if not yes_no_checker('Would you like to play again?: '):
            break

    print('------------------------------')
    print(f'Out of {guess_count} you got {correct_count} correct!\n'
          f'That is {(correct_count/guess_count) * 100}%')



