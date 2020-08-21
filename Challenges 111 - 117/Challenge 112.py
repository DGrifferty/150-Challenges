# 112
# Using the Books.csv file from program 111, ask the user to enter
# another record and add it to the end of the file. Display
# each row of the .csv file on a separate line.
from typing import List


def print_csv_table(lst: List, prt: bool = True):
	"""prints a csv table in a cleaner way"""

	string = ''

	for i in range(len(lst)):

			string += f'{lst[i]}'

	if prt:
		print(string)

	return string


if __name__ == '__main__':
	with open('Books.csv', 'r+') as f:
		table = f.readlines()
		print_csv_table(table)

		f.write(input('Enter a new record: ') + '\n')
