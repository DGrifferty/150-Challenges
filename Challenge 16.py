# 016
# Ask the user if it is raining and convert their answer to lower
# case so it doesn’t matter what case they type it in. If they answer
# “yes”, ask if it is windy. If they answer “yes” to this second
# question, display the answer “It is too windy for an umbrella”,
# otherwise display the message “Take an umbrella”.
# If they did not answer yes to the first question, display the answer
# “Enjoy your day”.
import sys

yes_list = ['yes', 'y', '1']
no_list = ['no', 'n']


def input_checker(string):
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

    question = 'Is it raining? '
    result = input_checker(question)

    if not result:
        print('Enjoy your day!')
        sys.exit()

    question = 'Is it windy? '
    result = input_checker(question)

    if result:
        print('It is too windy for an umbrella.')
        sys.exit()

    print('Take an umbrella')
