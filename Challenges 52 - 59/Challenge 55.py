# 055
# Randomly choose a number between 1 and 5. Ask the user to pick a
# number. If they guess correctly, display the message “Well done”,
# otherwise tell them if they are too high or too low and ask them
# to pick a second number. If they guess correctly on their second
# guess, display “Correct”, otherwise display “You lose”.

# VERY SIMILAR TO MY SOLUTION CHALLENGE 49
# where rather than trying to get the user guess 50, I made the
# user guess a random number between 0 and 50

import random

dev = False


def get_num(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


if __name__ == '__main__':

    comp_num: int = random.randint(0, 5)

    if dev:
        print(comp_num)

    guess_count = 0

    while True:
        guess_count += 1

        request = 'Enter your guess: '

        guess = get_num(request)

        if guess == comp_num:
            break
        elif guess < comp_num:
            print('Too low!')
        else:
            print('Too High!')

    print(f'You guessed right in {guess_count} guesses!')
