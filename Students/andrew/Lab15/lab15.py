"""http://www.gutenberg.org/cache/epub/8789/pg8789.txt"""
import requests
import os


PATH = "/school/Class_Runtime_Terrors/Students/andrew/Lab15/"


def get_book():
	try:
		print(os.getcwd())# Needed the path that the PATH variable should be set to since editing on different computers and files are on a network drive
		response = requests.get('http://www.gutenberg.org/files/8789/8789.txt')
		response.encoding = 'utf-8'  # set encoding to utf-8
		with open(f'{PATH}book.txt', 'wb') as f:
			f.write(response.content)
	except Exception as e:
		print(e)


def open_book(): # Opens book in terminal
	try:
		with open(f'{PATH}book.txt', "r") as book:
			size_to_read = 200
			book_content = book.read(size_to_read)
			while len(book_content) > 0:
				print(book_content)
				book_content = book.read(size_to_read)
	except (IOError, OSError, Exception) as e:
		print(e)
	else:
		pass



def make_dict():# Creates a dictionary from book.txt stores @path
	word_dict = {}
	word_list = []
	result = []
	count = 10
	with open(f'{PATH}book.txt') as book:
		for line in book:
			line = line.split()
			for word in line:
				word_list.append(word.lower())
		word_list.sort()
		# print(word_list) #Diagnostic use
	for word in word_list:
		word_dict[word] = word_list.count(word)
		sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
	print(f'The Top 10 Most Used Words in \n THE VISION OF HELL, PURGATORY, AND PARADISE BY DANTE ALIGHIERI')
	print('\n{:^2}{:^10}'.format('Word ', ' Count')) #	<-Thank you Python docs!
	while count > 0:# Probably could have used a for loop with range and so on
		print(f'{count} : {sorted_dict[count]}')
		result += sorted_dict[count]
		count -= 1
	


get_book()
#open_book()
make_dict()
