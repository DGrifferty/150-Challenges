# 059
# Display five colours and ask the user to pick one. If they pick the
# same as the program has chosen, say “Well done”, otherwise display
# a witty answer which involves the correct colour, e.g. “I bet you
# are GREEN with envy” or “You are probably feeling BLUE right now”.
# Ask them to guess again; if they have still not got it right, keep
# giving them the same clue and ask the user to enter a colour until
# they guess it correctly.


import random

dev = True


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

    colour_clue_dict = {
        'Blue': 'Look up!',
        'Red': 'Elephant party!',
        'Yellow': '______ pages!',
        'Green': 'Walking through the _____ _____ grass',
        'Orange': 'Colour named after a fruit!'
    }

    comp_guess = random.choice(list(colour_clue_dict.keys()))

    while True:

        if dev:
            print(comp_guess)

        user_guess = input('Guess a colour!: ')

        if user_guess.lower() != comp_guess.lower():
            print(colour_clue_dict[comp_guess])
        else:
            print('Correct!')
            if yes_no_checker('Would you like to play again?: '):
                comp_guess = random.choice(
                    list(colour_clue_dict.keys()))
            else:
                break


# TODO: Give different clues after each incorrect guess - store in list
# In dictionary then loop through that or random choice