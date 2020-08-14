# 056
# Randomly pick a whole number between 1 and 10. Ask the user to
# enter a number and keep entering numbers until they enter the
# number that was randomly picked.

import random


def get_num(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


comp_choice = random.randint(1, 10)

dev = True
if dev:
    print(comp_choice)

guess_count, user_choice = 0, -1

while user_choice != comp_choice:
    user_choice = get_num('Enter a number between 1 and 10 inclusive: ')
    guess_count += 1

    if user_choice != comp_choice:
        print('Incorrect!')

print(f'You guessed right in {guess_count} guesses!')
