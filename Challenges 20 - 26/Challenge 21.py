# 021
# Ask the user to enter their first name and then ask them to enter
# their surname. Join them together with a space between and display
# the name and the length of whole name.

from typing import List

# # Solution 1:
#
# while True:
#     try:
#         first_name = (input('Please enter your first name: '))
#         second_name = (input('Please enter your last name: '))
#
#         print(f'Hello {first_name} {second_name}!')
#
#         break
#     except Exception as e:
#         print(e)


# Solution 2
while True:
    try:
        name = list()
        name.append(input('Please enter your first name: '))
        name.append(input('Please enter your last name: '))

        print(f'Hello {" " .join(name)}!')

        break
    except Exception as e:
        print(e)


