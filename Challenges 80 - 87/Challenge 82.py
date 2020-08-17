# 082
# Show the user a line of text from your favourite poem and
# ask for a starting and ending point. Display the characters
# between those two points.

# very similar to challenge 74

from typing import List


def print_list(lst: List):
    """prints a list in a cleaner way"""

    string = ''

    for i in range(len(lst)):

        if i == len(lst) - 1:
            string += f'{lst[i]}.'
        else:
            string += f'{lst[i]}, '

        if i > 0:
            if i % 10 == 0:
                string += '\n'

    print(string)


def get_num_int(prompt: str) -> int:
    """Function to check if users input is an integer"""

    while True:
        try:
            number = int(input(prompt))

            return number

        except Exception as e:
            print(e)


def get_slice(sl):
    
    min, max = 0, len(sl)
    
    while True:
        
        start = get_num_int('Enter starting number of slice: ')

        if min <= start <= max:
            break
        else:
            print(f'Please enter a number between {min} and {max}')
            
    
    while True:
        
        end = get_num_int('Enter end number of slice: ')
        
        if start <= end <= max:
            break
        else:
            print(f'Please enter a number between {min} and {max}')

    return sl[start: end]
        

if __name__ == '__main__':
    
    poem = 'line from poem'

    print(poem)

    print_list(get_slice(poem))
    
    




