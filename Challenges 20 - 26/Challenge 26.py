# 026
# Pig Latin takes the first consonant of a word, moves it to the end of
# the word and adds on an “ay”. If a word begins with a vowel you just
# add “way” to the end. For example, pig becomes igpay, banana becomes
# ananabay, and aadvark becomes aadvarkway. Create a program that will
# ask the user to enter a word and change it into Pig Latin. Make sure
# the new word is displayed in lower case


def convert_pig(words):

    for index, value in enumerate(words):

        if words[index][0].lower() in 'aeiou':
            words[index] = words[index] + 'way'
            continue

        first_consonant = words[index][0]

        words[index] = words[index][1:] + first_consonant + 'ay'

    return words


if __name__ == '__main__':
    while True:

        try:
            words = input(
                'Please enter the words you want to convert to pig '
                'latin: ')

            words = words.split(' ')

            print(' '.join(convert_pig(words)))

            break

        except Exception as e:
            print(e)













