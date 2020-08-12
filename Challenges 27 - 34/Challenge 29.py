# 029
# Ask the user to enter an integer that is over 500.
# Work out the square root of that number and display
# it to two decimal places


def check_num_over(prompt: str, i: int = 500) -> float:
    """Function to check if users input is a number, over i"""

    while True:
        try:
            num = float(input(prompt))

            if num < 500:
                raise ValueError(f'Number must be over {i}!')

            return num

        except Exception as e:
            print(e)


if __name__ == '__main__':
    question = 'Please enter a number over 500: '

    print(f'{check_num_over(question) * 2:.2f}')

    # or ->
    # print(round(check_num_over(prompt)*2, 2))
