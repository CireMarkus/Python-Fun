'''This program is will sort a list of number and print the maximum number
'''
def max(numbers):
	numbers.remove(-999)
	swap = True
	temp = 0
	i = 0
	while swap == True:
		for i in range(len(numbers)):
			for j in range (0,len(numbers)-i-1):
				if numbers[j] > numbers[j+1]:
					temp = numbers[j]
					numbers[j] = numbers[j+1]
					numbers[j+1] = temp
				else:
					swap = False
	return numbers[0]


num = 0
nums = []
while num != -999:
	num = int(input('Please enter a number: '))
	nums.append(num)


sortnumbers=max(nums)

print('The min number in the list is: ',sortnumbers)
