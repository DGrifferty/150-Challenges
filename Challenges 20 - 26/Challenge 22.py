# 022
# Ask the user to enter their first name and surname in lower case.
# Change the case to title case and join them together.
# Display the finished result


while True:
    try:
        name = list()
        name.append(input('Please enter your first name in lower case'
                          ': '))
        name.append(input('Please enter your last name in lower case'
                          ': '))

        for index, value in enumerate(name):
            name[index] = name[index].title()

        print(f'Hello {" " .join(name)}!')

        break
    except Exception as e:
        print(e)
