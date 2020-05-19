class PhDguide:

	def __init__(self, name, email, students):
		self.name = name
		self.email = email
		self.students = students

	def putdata(self):
		print("Name: "+self.name)
		print("Email"+self.email)
		print("Students"+self.students)


	def add(self,student):
		students.append(student)

	def remove(self,studentName):
		for i in students:
			if(i.name==studentName):
				self.students.remove(i.name)
			else:
				print("student not found.") 
