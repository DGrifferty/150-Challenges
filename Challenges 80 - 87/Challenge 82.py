# 082
# Show the user a line of text from your favourite poem and
# ask for a starting and ending point. Display the characters
# between those two points.

# very similar to challenge 74




while True:
    start = get_num_int('Enter starting number: ')

    if 0 <= start <= 4:
        break
    else:
        print('Please enter a number between 0 and 4')

while True:
    end = get_num_int('Enter an end number: ')

    if 5 <= end <= 9:
        break
    else:
        print('Please enter a number between 5 and 9')

print(print_list(colour_list[start:end]))
