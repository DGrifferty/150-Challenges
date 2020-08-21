# 107
# Open the Names.txt file and display the data in Python.


with open('Names.txt', 'r') as f:
	names = f.readlines()

	for index, name in enumerate(names):  # To remove /n
		names[index] = name[:-1]

	print(names)
