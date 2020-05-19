class employee:
	"""The employee class"""
	def setdata(self):
		self.name = input('Enter name\t:')
		self.age = input('Enter age\t:')
	def getdata(self):
		print('Name\t:',self.name)
		print('Age\t:',self.age)
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __del__(self):
		print('Done')

e2 = employee('Eric',23)
e2.getdata()
print(e2.__doc__)	