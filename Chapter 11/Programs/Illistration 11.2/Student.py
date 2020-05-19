class Student:
	
	def __init__(self,name,email):
		self.name = name
		self.email = email

	def putdata(self):
		print("The student's name: " + self.name)
		print("The student's email: " + self.email)

class PhDguide:

	def __init__(self, name, email, students):
		self.name = name
		self.email = email
		self.students = students

	def putdata(self):
		print("Name: "+self.name)
		print("Email: "+self.email)
		self.printStudents()

	def printStudents(self):
		for i in self.students:
			print(i.name)


	def add(self,student):
		students.append(student)

	def remove(self,studentName):
		for i in self.students:
			if(i.name==studentName):
				self.students.remove(i)


a = Student("Eric", "Eric.edu")
b = Student("Shelly", "Shelly.edu")

tomStudents = [a,b]

b = PhDguide("tom", "tom.edu", tomStudents)
b.putdata()
b.remove("Shelly")
print("\n\n")
b.putdata()