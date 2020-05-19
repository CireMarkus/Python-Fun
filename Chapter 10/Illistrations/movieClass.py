class movie:
	def setdata(self):
		self.name = input('Enter name\t:')
		self.year = int(input('Enter year\t:'))
		self.genre = input('Enter gene\t:')
		self.director = input('Enter the name of the director\t:')
		self.producer = input('Enter the prodcer\t:')
		L = []
		item = input('Enter the name if the actor\t:')
		L.append(item)
		choice = input('Press \'y\' for more \'n\' to quit')
		while(choice == "y"):
			item = input('Enter name of the actor\t:')
			L.append(item)
			choice = input('Press \'y\' for more \'n\' to quit')
		self.actors = L
		self.musicDirector = input('Enter the name of the music director\t:')

	def getdata(self):
		print('Movie title\t:',self.name)
		print('Release year\t:',self.year)
		print('Genre\t:',self.genre)
		print('Director\t:',self.director)
		print('Producer\t:',self.producer)
		print('Music Director\t:',self.musicDirector)
		print('Actors\t:',end=' ')
		for i in self.actors:
			print(i,end=' ')

	def __init__(self):
		self.name ='Movie'
		self.year = 'YYYY'
		self.genre = 'Genre'
		self.director = 'XYZ'
		self.producer = 'ABC'
		self.musicDirector = 'LMN'
		self.actors = ['A1','A2','A3','A4']
m = movie()
m.getdata()

