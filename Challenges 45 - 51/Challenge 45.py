# 045
# Set the total to 0 to start with. While the total is 50 or less,
# ask the user to input a number. Add that number to the total and
# print the message “The total is… [total]”. Stop the loop when the
# total is over 50 .

def get_num(prompt: str) -> float:
    """Function to check if users input is a num"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


if __name__ == '__main__':

    total = 0
    while total <= 50:

        request = f'The total is currently: {total}.\n' \
                  f'Please enter the number you would like to add ' \
                  f'to it: '

        total += get_num(request)

    print(f'Final total: {total}')
