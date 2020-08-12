# 043
# Ask which direction the user wants to count (up or down). If they
# select up, then ask them for the top number and then count from 1 to
# that number. If they select down, ask them to enter a number below 20
# and then count down from 20 to that number. If they entered something
# other than up or down, display the message “I don’t understand”.

def get_num(prompt: str) -> float:
    """Function to check if users input is a num"""

    while True:
        try:
            num = int(input(prompt))

            return num

        except Exception as e:
            print(e)


def up_down_checker(string: str) -> bool:
    """Function to check if user wants to go up or down by asking
    for their in put, up = True, down = False"""

    up_list = ['up', 'u', '1']
    down_list = ['down', 'd', '0']

    while True:
        try:

            answer = input(string)

            if answer.lower() not in up_list and answer.lower() \
                    not in down_list:
                print('Please enter up or down')
                continue
            elif answer.lower() in up_list:
                return True
            else:
                return False

        except Exception as e:
            print(e)


if __name__ == '__main__':

    question = 'Would you like to count up or down? '
    if up_down_checker(question):
        request = 'Please enter what number you would like to count' \
                  ' up to: '
        num = get_num(request)
        for i in range(num + 1):
            print(i)
    else:
        request = 'Please enter what number below 20 you would ' \
                  'like to count down to: '
        num = 21
        while num > 19:
            num = get_num(request)

        for i in range(20, num - 1, -1):
            print(i)
