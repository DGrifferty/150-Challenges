# 020
# Ask the user to enter their first name and
# then display the length of their name.
from typing import List


while True:
    try:
        name: str = input('Please enter your name: ')
        name: List[str] = name.split(' ')

        first_name: str = name[0]

        print(f'Hello {first_name} you have {len(first_name)} '
              f'characters in your first name.')
        break
    except Exception as e:
        print(e)


