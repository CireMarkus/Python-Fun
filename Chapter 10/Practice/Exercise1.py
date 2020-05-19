class Intern:
	def setdata(self):
		self.firstname = str(input('Enter the intern\'s first name\t:'))
		self.lastname = str(input('Enter the intern\'s last name\t:'))
		self.address = str(input('Enter the intern\'s address\t:'))
		self.mobilenumber = str(input('Enter the intern\'s mobile number\t:'))
		self.email = str(input('Enter the interns\'s email address\t:'))

	def getdata(self):
		print('The intern\'s information is:')
		print('Name\t:',self.firstname,'',self.lastname)
		print('Address\t:',self.address)
		print('Phone number\t:',self.mobilenumber)
		print('E-mail\t:',self.email)

i1 = Intern()
i1.setdata()
i1.getdata()