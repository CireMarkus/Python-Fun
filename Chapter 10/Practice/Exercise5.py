class Book:
	#def __init__(self):

	def setdata(self):
		self.title = input('Enter the title of the book\t:')
		self.publisher = input('Enter the publisher of the book\t:')
		self.year = input('Enter the year the book was published\t:')
		self.isbn = input('Enter the ISBN of the book\t:')
		self.authors = []
		go = True
		while go == True:
			self.authors.append(str(input('Enter an author if the book\t:')))
			choice = str(input('Are there anymore authors? Enter Y or N\t:'))
			if choice.upper() == 'N':
				go = False
			else:
				go = True

	def getdata(self):
		print('Title: ',self.title)
		print('Publisher: ',self.publisher)
		print('Year: ',self.year)
		print('ISBN: ',self.isbn)
		print('Author(s)',self.authors)
	def __del__(self):
		print('This is the decontructor.')

b1 = Book()
b1.setdata()
b1.getdata()