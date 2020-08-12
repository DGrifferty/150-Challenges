# 035
# Ask the user to enter their name and then
# display their name three times.

try:
    name = input('Enter your name: ')

    for i in range(3):
        print(name)

except Exception as e:
    print(e)


