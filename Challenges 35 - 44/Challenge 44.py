# 044
# Ask how many people the user wants to invite to a party.
# If they enter a number below 10, ask for the names and after
# each name display “[name] has been invited”. If they enter a number
# which is 10 or higher, display the message “Too many people”.

def get_num(prompt: str) -> float:
    """Function to check if users input is a num"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


if __name__ == '__main__':

    question = 'How many people would you like to invite to the party?'

    invites = get_num(question)

    if invites < 10:
        for i in range(invites):
            name = input(f'Who is invite number {i+1}?: ')
            print(f'{name.title()} has been invited!')

