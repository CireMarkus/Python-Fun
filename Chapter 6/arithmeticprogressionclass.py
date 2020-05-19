class progression:
	def __init__(self):
		self.num = int(input('Enter the number of terms\t:'))
		self.a = int(input('Enter the first term\t:'))
		self.d = int(input('Enter the common difference\t:'))

	def __iter__(self):
			return self

	def sequence(self):
			for i in range (self.num):
				print(self.a+i*self.d)

y = progression

y.__init__(y)
y.sequence(y)

