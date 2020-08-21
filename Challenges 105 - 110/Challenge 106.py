# 106
# Create a new file called “Names.txt”. Add five names to the document,
# which are stored on separate lines. Once you have run the program,
# look in the location where your program is stored and check
# that the file has been created properly


names_lst = ['Jeff', 'Fred', 'Bob', 'Jack', 'Jeff2']

with open('Names.txt', 'w') as f:
	for index, value in enumerate(names_lst):

		if index < len(names_lst) - 1:
			parsed_name = value + '\n'
			f.write(parsed_name)
		else:
			f.write(value)




