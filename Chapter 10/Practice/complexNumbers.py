from fractions import Fraction

class Complex_number:


	def setdata(self):
		self.real_part = input('Enter the real part of the number\t:')
		self.ima_part = input('Enter the imaginary part of the number\t:')

	def getdata(self):
		print('The complex number is: {}+({})i'.format(self.real_part,self.ima_part))
	
	def __init__(self,real = 0,imaginary = 0):
		self.real_part = real
		self.ima_part = imaginary

	#def __del__(self):
		#print(__object__.__name__,'Deleted')



def add(num1,num2):
	c3 = Complex_number(num1.real_part+num2.real_part,num1.ima_part+num2.ima_part)
	return c3

def sub(num1,num2):
	c3 = Complex_number(num1.real_part - num2.real_part,num1.ima_part - num2.ima_part)
	return c3

def multiply(num1,num2):
	c1 = Complex_number((num1.real_part*num2.real_part)-(num1.ima_part*num2.ima_part),(num1.real_part*num2.ima_part)+(num1.ima_part*num2.real_part))
	return c1

def div(num1,num2):
	c1 = Complex_number(num2.real_part,-(num2.ima_part)) #Creates the conjugate of the denominator 
	c2 = multiply(num1,c1) #mutiplies the top numerator by the conjugate 
	c3 = multiply(num2,c1) #multiplies the denominator by the conjugate

	if(c3.ima_part == 0):
		#Divides by the real_part of the denominator if the ima_part equals zero
		return Complex_number(Fraction(c2.real_part/c3.real_part).limit_denominator(),Fraction(c2.ima_part/c3.real_part).limit_denominator())
	else:
		#divides each side if the real_part of the denominator does not equal zero
		return Complex_number(Fraction(c2.real_part/c3.real_part).limit_denominator(),Fraction(c2.ima_part/c3.ima_part).limit_denominator())


c1 = Complex_number(3,4)
c2 = Complex_number(-5,6)

c3 = add(c1,c2)
c4 = sub(c1,c2)
c5 = multiply(c1,c2)
c6 = div(c1,c2)

c3.getdata()
c4.getdata()
c5.getdata()
c6.getdata()