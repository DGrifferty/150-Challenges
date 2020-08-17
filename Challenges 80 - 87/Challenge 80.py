# 080
# Ask the user to enter their first name and then display the length of
# their first name. Then ask for their surname and display the length of
# their surname. Join their first name and surname together with a space
# between and display the result. Finally, display the length of their
# full name (including the space).

# Very simple, getting all names together at once makes more sense.
# Taking code - from challenge 2

from typing import List

while True:
    try:
        name: str = input('Please enter your full name: ')
        length_full_name = len(name)
        names: List[str] = name.split(' ')

        first_name: str = names[0]
        middle_names: str = names[1:-1]
        last_name: str = names[-1]

        print(f'Hello {first_name.title()}', end=' ')

        for i in range(len(middle_names)):
            print(middle_names[i].title(), end=' ')

        print(f'{last_name.title()}')

        break
    except Exception as e:
        print(e)


print(f'Your first name has {len(first_name)} characters')
if middle_names:
    if len(middle_names) > 1:
        for value in middle_names:
            print(f'Middle name \'{value.title()}\' has {len(value)}'
                  ' characters')
    else:
        print(f'Your middle name has '
              f'{len(str(middle_names[0]))} characters')

print(f'Your surname name has {len(last_name)} characters')

print(f'Your full name has {length_full_name} '
      f'characters including spaces.')


