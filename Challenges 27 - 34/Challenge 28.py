# 027
# Ask the user to enter a number with lots of decimal places.
# Multiply this number by two and display the answer.

# 028
# Update program 027 so that it will display the answer to two
# decimal places.


def check_num(prompt: str) -> float:
    """Function to check if users input is a number"""

    while True:
        try:
            num = float(input(prompt))

            return num

        except Exception as e:
            print(e)


if __name__ == '__main__':
    question = 'Please enter a number: '

    print(f'{check_num(question) * 2:.2f}')

    # or ->
    # print(round(check_num(prompt)*2, 2))
