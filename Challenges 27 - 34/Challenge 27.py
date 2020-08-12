# 027
# Ask the user to enter a number with lots of decimal places.
# Multiply this number by two and display the answer.


def check_num(prompt: str) -> float:
    """Function to check if users input is a num"""

    while True:
        try:
            num = float(input(prompt))

            return num

        except Exception as e:
            print(e)

if __name__ == '__main__':

    prompt = 'Please enter a number: '

    print(check_num(prompt)*2)