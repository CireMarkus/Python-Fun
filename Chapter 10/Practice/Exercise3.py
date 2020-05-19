class Intern:
	def __init__(self,fname,lname,add,mobile,e):
		self.firstname = fname
		self.lastname = lname
		self.address = add
		self.mobilenumber = mobile
		self.email = e

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

i1 = Intern('Eric','Washington','1706 Thornhollow Dr.','361-400-9079','Mrkimjarrow95@gmail.com')
#i1.setdata()
i1.getdata()