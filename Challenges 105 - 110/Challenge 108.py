# 108
# Open the Names.txt file. Ask the user to input a new name.
# Add this to the end of the file and display the entire file.


with open('Names.txt', 'r+') as f:
	names = f.readlines()

	for index, name in enumerate(names):  # To removing /n
		names[index] = name[:-1]

	print(names)

	names.append(input('Enter a name: '))

	parsed_name = '\n' + names[-1]
	f.write(parsed_name)

	print(names)
