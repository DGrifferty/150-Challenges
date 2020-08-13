# 049
# Create a variable called compnum and set the value to 50. Ask the user
# to enter a number. While their guess is not the same as the compnum
# value, tell them if their guess is too low or too high and ask them to
# have another guess. If they enter the same value as compnum, display
# the message “Well done, you took [count] attempts”.
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

    comp_num: int = random.randint(0, 50)
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
