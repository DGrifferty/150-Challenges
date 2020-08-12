# 040
# Ask for a number below 50 and then count down from 50 to that number,
# making sure you show the number they entered in the output.

def check_num(prompt: str) -> float:
    """Function to check if users input is an integer"""

    while True:
        try:
            num = int(input(prompt))

            return num

        except Exception as e:
            print(e)


if __name__ == '__main__':

    request = 'Enter a number to count down from: '

    num = check_num(request)

    for i in range(num, -1, -1):
        print(i)

