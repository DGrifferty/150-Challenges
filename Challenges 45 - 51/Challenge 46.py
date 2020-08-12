# 046
# Ask the user to enter a number. Keep asking until they enter a
# value over 5 and then display the message “The last number you
# entered was a [number]” and stop the program.

def get_num(prompt: str) -> float:
    """Function to check if users input is a number"""

    while True:
        try:
            number = float(input(prompt))

            return number

        except Exception as e:
            print(e)


if __name__ == '__main__':
    num = 0
    request = 'Enter a number: '
    while num <= 5:
        num = get_num(request)

    print(f'The last number you entered was {num}.')





