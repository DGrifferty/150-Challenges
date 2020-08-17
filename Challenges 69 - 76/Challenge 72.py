# 072
# Create a list of six school subjects. Ask the user which of these
# subjects they don’t like. Delete the subject they have chosen
# from the list before you display the list again.
from typing import List


def get_input_list(lst: List[str], prompt: str) -> bool:

    lstlow = list((x.lower() for x in lst))

    while True:
        try:

            user_input = input(prompt)
            if user_input.lower() in lstlow:
                return lst[lstlow.index(user_input)]
            else:
                continue

        except Exception as e:
            print(e)


def print_list(lst: List[float]):
    """returns a string allowing you to print a list in a cleaner way"""

    string = ''

    for i in range(len(lst)):

        if i == len(lst) - 1:
            string += f'{lst[i]}.'
        else:
            string += f'{lst[i]}, '

        if i > 0:
            if i % 10 == 0:
                string += '\n'

    return string



if __name__ == '__main__':


    subjects =  ['Maths', 'English', 'PE', 'Geography']

    print(print_list(subjects))

    bad_subject = get_input_list(subjects, 'Please enter the name of '
                                           'the subject you would like '
                                           'to remove: ')
    subjects.remove(bad_subject)

    print(print_list(subjects))




