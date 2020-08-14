# 057
# Update program 056 so that it tells the user if they are
# too high or too low before they pick again.

# Very similar to challenge 55 and 49

import random

dev = True


def get_num(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


if __name__ == '__main__':

    comp_num: int = random.randint(0, 10)

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