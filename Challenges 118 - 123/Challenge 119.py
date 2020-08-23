# 119
# Define a subprogram that will ask the user to pick a low and
# a high number, and then generate a random number between those
# two values and store it in a variable called “comp_num”.
# Define another subprogram that will give the instruction
# “I am thinking of a number…” and then ask the user to guess the
# number they are thinking of. Define a third subprogram that will
# check to see if the comp_num is the same as the user’s guess.
# If it is, it should display the message “Correct, you win”,
# otherwise it should keep looping, telling the user if they
# are too low or too high and asking them to guess again
# until they guess correctly.


import random


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))
            return number

        except Exception as e:
            print(e)


def low_high_random() -> int:
    low_num = get_num_int('Enter the lowest number you'
                          ' want the random number to be: ')
    high_num = get_num_int('Enter the highest number you want the '
                           'random '
                           ' number to be: ')

    return random.randint(low_num, high_num)


def check_guess(to_guess: int, guess: int) -> bool:
    if to_guess == guess:
        print('Correct, you win!')
        return True
    elif to_guess > guess:
        print('Higher!')
    else:
        print('Lower!')
    return False


def get_user_guess(compnum: int):
    print('I am thinking of a number...')
    while True:
        user_guess = get_num_int('Enter your guess: ')

        if check_guess(compnum, user_guess):
            break


if __name__ == '__main__':
    get_user_guess(low_high_random())
