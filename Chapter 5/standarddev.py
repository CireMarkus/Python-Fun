import math


def deviation(numbers):
	mu = 0 #this will hold the mean of the original numbers entered.

	#print("This is the list of numbers: ", numbers), debug
	for i in range (len(numbers) - 1):
		mu += numbers[i] 

	#print("This is the total of numbers: ",mu), debug
	
	mu = (math.ceil(mu/len(numbers))) #This finds the mean of the original numbers entered

	#print("This is the total of mu: ",mu), debug
	
	newNums = [] #holds the values of the original numbers 

	for i in range (len(numbers) - 1):
		newNums.append((numbers[i] - mu)**2) #subtracts the mean of the orignal numbers from each original number and squares the difference

	#print("This is the list of newNums: ", newNums), debug

	summation = 0

	for i in newNums:
		summation+=i

	#print("This is the total of summation: ",summation), debug
	deviation = math.sqrt(summation/len(newNums))

	return deviation



print('Please enter a list of numbers, when done enter -1 to indicate completion')

num = 0

numberList = []

while num != -1:
	num = int(input("Enter numbers here: "))

	numberList.append(num)

print("The standard deviation for the numbers you entered is: ",deviation(numberList))