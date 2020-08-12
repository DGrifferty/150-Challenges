# 002
# Ask for the user’s first name and then ask for their surname and
# display the output message Hello [First Name] [Surname].
from typing import List
# Solution 1:
# while True:
#     try:
#         First_name = input('Please enter your first name:')
#         Surname = input('Please enter your surname:')
#         break
#     except Exception as e:
#         print(e)
#
# print(f'Hello {First_name}')

# Solution 2:
while True:
    try:
        name: str = input('Please enter your full name: ')
        name: List[str] = name.split(' ')

        first_name: str = name[0]
        middle_names: str = name[1:-1]
        last_name: str = name[-1]

        print(f'Hello {first_name} {last_name}')
        break
    except Exception as e:
        print(e)
