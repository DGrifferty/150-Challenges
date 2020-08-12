# 039
# Ask the user to enter a number between 1 and 12 and
# then display the times table for that number.

def check_num(prompt: str) -> float:
    """Function to check if users input is an integer"""

    while True:
        try:
            num = int(input(prompt))

            return num

        except Exception as e:
            print(e)


