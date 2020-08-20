# 104 After gathering the four names, ages and shoe sizes,
# ask the user to enter the name of the person they want to
# remove from the list. Delete this row from the data and
# display the other rows on separate lines.

from typing import Dict


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


def print_dic_of_dics(dic: Dict):

    for key in dic.keys():
        keys = list(dic[key].keys())
        print(key, end=' : ')
        for i in keys:
            if keys.index(i) == len(keys) - 1:
                print(i, end=' = ')
                print(dic[key][i], end='.\n')
            else:
                print(i, end=' = ')
                print(dic[key][i], end=', ')


if __name__ =='__main__':

    # Getting data
    name_age_size = dict()

    for i in range(4):

        name = input(f'Enter name number {i+1}: ')

        name_age_size[name] = {'Age': get_num_int('Enter their age: '),
                               'Shoe size': get_num_int('Enter their '
                                                        'shoe size: ')}

    print_dic_of_dics(name_age_size)

    while True:

        name = input('Enter the name: ')

        if name in name_age_size:
            del name_age_size[name]
            print(f'{name} removed!')
            break

    print_dic_of_dics(name_age_size)





