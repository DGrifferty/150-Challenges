# 111
# Create a .csv file that will store the following data. Call it
# “Books.csv”.

with open('Books.csv', 'w') as f:

	table = 'To Kill a Mokingbird, Harper Lee, 1960\n' \
	        'A Brief History of time, Stephen Hawking, 1988\n' \
	        'The Great Gatsby, F. Scott Fitzgerald, 1922\n' \
	        'The man who mistook his wife for a hat, Oliver Scaks, 1985\n' \
	        'Pride and Prejudice, Jane Austen, 1813\n'

	f.write(table)
