# 025
# Ask the user to enter their first name. If the length of their first
# name is under five characters, ask them to enter their surname and
# join them together (without a space) and display the name in upper
# case. If the length of the first name is five or more characters,
# display their first name in lower case.

def length(s1: str, l: int = 5) -> bool:
    if len(s1) < l:
        return True
    return False


while True:
    try:

        first_name: str = input('Please enter your first name: ')
        if length(first_name):
            surname: str = input('Please enter your surname: ')
            print(first_name.upper(), surname.upper())
            break
        else:
            print(first_name.lower())
        break

    except Exception as e:
        print(e)
