import math

def median():
	num = int(input('Enter how many numbers will be in the list: '))

	numbers = []

	for i in range(num):
		numbers.append(int(input("Please enter the "+str(i)+" number")))

	if(num%2 !=0):
		print("The median number is "+str(numbers[math.floor(len(numbers)/2)]))
	else:
		print("The median numbers are "+str(numbers[math.floor(len(numbers)/2) - 1])+ " and " + str(numbers[int(math.floor(len(numbers)/2))]))


median()