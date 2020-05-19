from collections import Counter

#function to calculate which number is entered the most.
def mode ():
	num = int(input('How many numbers would you like to enter: '))
	nums = []

	for i in range (0,num):
		nums.append(int(input('\n\nPlease enter a number: ')))

	mode = Counter(nums)

	print('You entered the number ', str(mode.most_common(1))[2]," the most.")



mode()