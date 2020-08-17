# 087
# Ask the user to type in a word and then display it
# backwards on separate lines.

word = list(i for i in list(input('Enter your word: ')))

for index, value in enumerate(word):
    print(word[-1 - index])

