# 042
# Set a variable called total to 0. Ask the user to enter five numbers
# and after each input ask them if they want that number included.
# If they do, then add the number to the total. If they do not want
# it included, don’t add it to the total. After they have entered
# all five numbers, display the total.


def check_num(prompt: str) -> float:
    """Function to check if users input is a num"""

    while True:
        try:
            num = float(input(prompt))

            return num

        except Exception as e:
            print(e)


def yes_no_checker(string):
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

    no_of_numbers = 5
    summed = []

    for i in range(no_of_numbers):
        request = f'Enter number {i+1}: '
        num = check_num(request)
        question = f'Would you like to add {num} to the total?: '

        if yes_no_checker(question):
            summed.append(num)

    print(f'Adding up numbers: {summed}')
    print(f'Total: {sum(summed)}')







