'''This program finds the mean of a set of numbers entered by the user.'''

print('This program finds the mean of a aset of numbers entered by you.')

total = int(input('Please enter the how mawny numbers you plan to enter: '))

numList = []

for i in range (total):
	num = int(input('Please enter a number: '))

	numList.append(num)


allNum = 0

for i in (numList):
	allNum += i

mean = allNum/len(numList)

print('The mean of the numbers is ' + str(int(mean)))