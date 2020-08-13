# 050
# Ask the user to enter a number between 10 and 20. If they enter a
# value under 10, display the message “Too low” and ask them to try
# again. If they enter a value above 20, display the message “Too high”
# and ask them to try again. Keep repeating this until they enter a
# value that is between 10 and 20 and then display the message
# “Thank you”


def get_num(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


if __name__ == '__main__':

    between = [10, 20]

    while True:

        request = f'Enter a number between {between[0]} and ' \
                  f'{between[1]}: '

        guess = get_num(request)

        if between[0] < guess < between[1]:
            break
        elif guess <= between[0]:
            print('Too low!')
        else:
            print('Too High!')

    print(f'Thank you.')

