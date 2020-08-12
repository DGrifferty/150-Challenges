# 015
# Ask the user to enter their favourite colour. If they enter “red”,
# “RED” or “Red” display the message “I like red too”, otherwise display
# the message “I don’t like [colour], I prefer red”

while True:
    try:

        spl = list()

        colour = input('Please enter you favourite colour: ')

        for char in colour.lower():
            spl.append(char)

        for letter in spl:
            if letter not in 'abcdefghijklmnopqrstuv':
                raise Exception('Please enter letters only')

        if colour.lower() == 'red':
            print('I also like red')
        else:
            print(f'I do not like {colour}')

        break

    except Exception as e:
        print(e)
