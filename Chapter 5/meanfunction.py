def mean(list):
	total = 0
	for i in list:
		total = total+ i
	return (total/len(list))

user = input('Please enter the numbers: ')

data = [int(i) for i in str(user)]

print('The mean of the numbers you entered is ' , mean(data))	