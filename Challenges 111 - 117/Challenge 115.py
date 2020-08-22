# 115
# Using the Books.csv file, display the data in the
# file along with the row number of each.
from typing import List


def print_csv_table(lst: List, print_row_num: bool = False,
                    prt: bool = True):
	"""prints a csv table in a cleaner way"""

	string = ''

	if print_row_num:
		for i in range(len(lst)):
			string += f'{i+1} {lst[i]}'
	else:
		for i in range(len(lst)):
			string += f'{lst[i]}'

	if prt:
		print(string)

	return string


if __name__ == '__main__':

	with open('Books.csv', 'r+') as f:
		table = f.readlines()
		print_csv_table(table, print_row_num=True)






