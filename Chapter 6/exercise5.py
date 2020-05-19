from fractions import Fraction

def geometric(a,r,n):
	i = 0
	while i <n:
		#Having issues with the program printing 1/3
		yield Fraction.from_float(1 /(a+i*r))

		i+=1

for i in geometric(1,1,3):
	print(i)