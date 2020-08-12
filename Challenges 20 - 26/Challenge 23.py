# 023
# Ask the user to type in the first line of a nursery rhyme and display
# the length of the string. Ask for a starting number and an
# ending number and then display just that section of the text
# (remember Python starts  counting from 0 and not 1).

rhyme = list()
while True:
    try:
        if not rhyme:
            rhyme = input('Please enter the first line of a nursery '
                          'rhyme: ')
            print(f'There are {len(rhyme)} characters in that line')

        from_to = input('Please type in the starting character'
                        'you want to the final character: ')

        from_to = from_to.split(' ')

        for index, value in enumerate(from_to):
            from_to[index] = int(value)

        print(rhyme[from_to[0] - 1:from_to[1] + 1])

        break

    except Exception as e:
        print(e)
